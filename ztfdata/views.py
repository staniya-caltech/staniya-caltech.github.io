from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages

from ztfdata.scripts.pandas_sql import DataIngestion

from .models import PandasData
from django.core.files.storage import FileSystemStorage
import os
import json
import pandas as pd
# Create your views here.


def UploadView(request):
    # declaring template
    template_name = "upload.html"
    data = PandasData.objects.all()
    # prompt is a context variable that can have different values
    # depending on their context
    prompt = {
        'order': 'Order of the dat file parameters should be index, field, ccdid, qid, filter, pid, infobitssci, sciinpseeing, scibckgnd, scisigpix, zpmaginpsci, zpmaginpsciunc, zpmaginpscirms, clrcoeff, clrcoeffunc, ncalmatches, exptime, adpctdif1, adpctdif2, diffmaglim, zpdiff, programid, jd, rfid, forcediffimflux, forcediffimfluxunc, forcediffimsnr, forcediffimchisq, forcediffimfluxap, forcediffimfluxuncap, forcediffimsnrap, aperturecorr, dnearestrefsrc, nearestrefmag, nearestrefmagunc, nearestrefchi, nearestrefsharp, refjdstart, refjdend, procstatus',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template_name, prompt)
    elif request.method == 'POST':
        rel_filepath = request.FILES['file']
        if not rel_filepath.name.endswith('.dat') or not rel_filepath.name.endswith('.phot'):
            messages.error(request, 'THIS IS NOT A DAT OR PHOT FILE')
        base_dir = os.path.join(os.getcwd(), 'uploaded_data')
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        if "ps1" in rel_filepath.name:
            fs = FileSystemStorage(location=os.path.join(base_dir, 'Andrew'))
            filename = fs.save(rel_filepath.name, rel_filepath)
            uploaded_file_path = fs.path(filename)
            pipeline = "a"
        elif "mrozpipe" in rel_filepath.name:
            fs = FileSystemStorage(location=os.path.join(base_dir, 'mrozpipe'))
            filename = fs.save(rel_filepath.name, rel_filepath)
            uploaded_file_path = fs.path(filename)
            pipeline = "m"
        elif "ztffps" in rel_filepath.name:
            fs = FileSystemStorage(location=os.path.join(base_dir, 'ztffps'))
            filename = fs.save(rel_filepath.name, rel_filepath)
            uploaded_file_path = fs.path(filename)
            pipeline = "z"
        else:
            raise Exception(
                "The input is not a product of a valid photometry pipeline")

        cleaned_data = DataIngestion(uploaded_file_path, pipeline)
        try:
            cleaned_data.process_pandas_to_sql()
            os.remove(uploaded_file_path)
        except BaseException as e:
            messages.error(request, f"Process failed due to the following error: \n {e}")

        context = {}
        return render(request, template_name, context)


def DataView(request):
    data = PandasData.objects.all()
    context = {
        "forced_photometry": data
    }
    df_assets = pd.DataFrame(list(data.values()))
    # parsing the DataFrame in json format.
    json_records = df_assets.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'table.html', context)
