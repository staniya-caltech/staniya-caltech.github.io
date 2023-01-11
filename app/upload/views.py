from django.shortcuts import render
from django.contrib import messages

from upload.scripts.pandas_sql import DataIngestion

from .models import AndrewData, MROZData, ZTFFPSData
from django.core.files.storage import FileSystemStorage
import os
import json
import pandas as pd


def UploadView(request):
    """
    When Django handles a file upload, the file data ends up placed in request.FILES
    """
    template_name = "upload.html"
    ztffps_data = ZTFFPSData.objects.all()
    mroz_data = MROZData.objects.all()
    andrew_data = AndrewData.objects.all()
    # prompt is a context variable that can have different values depending on their context
    prompt = {
        "order": "ZTFFPS file parameters should be: index, field, ccdid, qid, filter, pid, infobitssci, \
            sciinpseeing, scibckgnd, scisigpix, zpmaginpsci, zpmaginpsciunc, zpmaginpscirms, clrcoeff, clrcoeffunc, \
            ncalmatches, exptime, adpctdif1, adpctdif2, diffmaglim, zpdiff, programid, jd, rfid, forcediffimflux, \
            forcediffimfluxunc, forcediffimsnr, forcediffimchisq, forcediffimfluxap, forcediffimfluxuncap, \
            forcediffimsnrap, aperturecorr, dnearestrefsrc, nearestrefmag, nearestrefmagunc, nearestrefchi, \
            nearestrefsharp, refjdstart, refjdend, procstatus \n\n \
            MROZ file parameters should be: bjd mag magerr diffimflux diffimfluxunc flag filterid exptime pid \
            field ccd quad status infobits seeing zpmagsci zpmagsciunc zpmagscirms clrcoeff clrcoeffunc maglim \
            airmass nps1matches \n\n \
            ANDREW file parameters should be: PS1_ID MJD Mag_ZTF Mag_err Flux Flux_err g_PS1 r_PS1 i_PS1 Stargal infobits",
        "ztffps_profile": ztffps_data,
        "mroz_profile": mroz_data,
        "andrew_profile": andrew_data,
    }

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template_name, prompt)
    # POST request parses the contents of the uploaded file and appends it to PostgreSQL
    elif request.method == "POST":
        rel_filepath = request.FILES["file"]
        # Check that the file is of the correct type
        if not rel_filepath.name.endswith(".dat") or not rel_filepath.name.endswith(
            ".phot"
        ):
            messages.error(request, "THIS IS NOT A DAT OR PHOT FILE")
        # In order to parse the contents of the uploaded file, the file has to be saved temporarily
        base_dir = os.path.join(os.getcwd(), "uploaded_data")
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        if "ps1" in rel_filepath.name:
            fs = FileSystemStorage(location=os.path.join(base_dir, "andrew"))
            filename = fs.save(rel_filepath.name, rel_filepath)
            uploaded_file_path = fs.path(filename)
            pipeline = "a"
        elif "mrozpipe" in rel_filepath.name:
            fs = FileSystemStorage(location=base_dir)
            filename = fs.save(rel_filepath.name, rel_filepath)
            uploaded_file_path = fs.path(filename)
            pipeline = "m"
        elif "ztffps" in rel_filepath.name:
            fs = FileSystemStorage(location=base_dir)
            filename = fs.save(rel_filepath.name, rel_filepath)
            uploaded_file_path = fs.path(filename)
            pipeline = "z"
        else:
            raise Exception("The input is not a product of a valid photometry pipeline")
        # create a DataIngestion object so that the uploaded data can be converted from a Pandas DataFrame to PostgreSQL
        cleaned_data = DataIngestion(uploaded_file_path, pipeline)

        # run process_pandas_to_sql() to append the ingested data to PostgreSQL
        # remove the saved file to conserve memory
        try:
            cleaned_data.process_pandas_to_sql()
        except Exception as e:
            messages.error(
                request, f"Process failed due to the following error: \n {e}"
            )
        os.remove(uploaded_file_path)
        os.rmdir(base_dir)
        context = {}
        return render(request, template_name, context)


def DataView(request):
    """
    Read data from PostgreSQL database table into a pandas dataframe and display it
    in a custom html table defined in table.html
    """
    ztffpsdata = ZTFFPSData.objects.all()
    mrozdata = MROZData.objects.all()
    andrewdata = AndrewData.objects.all()
    context = {
        "ztffps_forced_photometry": ztffpsdata,
        "mroz_forced_photometry": mrozdata,
        "andrew_forced_photometry": andrewdata,
    }
    # For ztffps
    ztffps_assets = pd.DataFrame(list(ztffpsdata.values()))
    # parsing the DataFrame in json format.
    ztffps_json_records = ztffps_assets.reset_index().to_json(orient="records")
    ztffps_data = []
    ztffps_data = json.loads(ztffps_json_records)

    # For mroz
    mroz_assets = pd.DataFrame(list(mrozdata.values()))
    # parsing the DataFrame in json format.
    mroz_json_records = mroz_assets.reset_index().to_json(orient="records")
    mroz_data = []
    mroz_data = json.loads(mroz_json_records)

    # For andrew
    andrew_assets = pd.DataFrame(list(andrewdata.values()))
    # parsing the DataFrame in json format.
    andrew_json_records = andrew_assets.reset_index().to_json(orient="records")
    andrew_data = []
    andrew_data = json.loads(andrew_json_records)

    context = {"ztffps": ztffps_data, "mroz": mroz_data, "andrew": andrew_data}
    return render(request, "table.html", context)
