from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages

from ztfdata.scripts.pandas_sql import DataIngestion

from .models import PandasData
from django.core.files.storage import FileSystemStorage
import os
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
        cleaned_data.process_pandas_to_sql()
        # for model in df.itertuples():
        #     _, created = PandasData.objects.update_or_create(
        #         index=model.index,
        #         field=model.field,
        #         ccdid=model.ccdid,
        #         qid=model.qid,
        #         filter=model.qid,
        #         pid=model.pid,
        #         infobitssci=model.infobitssci,
        #         sciinpseeing=model.sciinpseeing,
        #         scibckgnd=model.scibckgnd,
        #         scisigpix=model.scisigpix,
        #         zpmaginpsci=model.zpmaginpsci,
        #         zpmaginpsciunc=model.zpmaginpsciunc,
        #         zpmaginpscirms=model.zpmaginpscirms,
        #         clrcoeff=model.clrcoeff,
        #         clrcoeffunc=model.clrcoeffunc,
        #         ncalmatches=model.ncalmatches,
        #         exptime=model.exptime,
        #         adpctdif1=model.adpctdif1,
        #         adpctdif2=model.adpctdif2,
        #         diffmaglim=model.diffmaglim,
        #         zpdiff=model.zpdiff,
        #         programid=model.programid,
        #         jd=model.jd,
        #         rfid=model.rfid,
        #         forcediffimflux=model.forcediffimflux,
        #         forcediffimfluxunc=model.forcediffimfluxunc,
        #         forcediffimsnr=model.forcediffimsnr,
        #         forcediffimchisq=model.forcediffimchisq,
        #         forcediffimfluxap=model.forcediffimfluxap,
        #         forcediffimfluxuncap=model.forcediffimfluxuncap,
        #         forcediffimsnrap=model.forcediffimsnrap,
        #         aperturecorr=model.aperturecorr,
        #         dnearestrefsrc=model.dnearestrefsrc,
        #         nearestrefmag=model.nearestrefmag,
        #         nearestrefmagunc=model.nearestrefmagunc,
        #         nearestrefchi=model.nearestrefchi,
        #         nearestrefsharp=model.nearestrefsharp,
        #         refjdstart=model.refjdstart,
        #         refjdend=model.refjdend,
        #         procstatus=model.procstatus,
        #         defaults={'index': model.index,
        #                   'field': model.field,
        #                   'ccdid': model.ccdid,
        #                   'qid': model.qid,
        #                   'filter': model.qid,
        #                   'pid': model.pid,
        #                   'infobitssci': model.infobitssci,
        #                   'sciinpseeing': model.sciinpseeing,
        #                   'scibckgnd': model.scibckgnd,
        #                   'scisigpix': model.scisigpix,
        #                   'zpmaginpsci': model.zpmaginpsci,
        #                   'zpmaginpsciunc': model.zpmaginpsciunc,
        #                   'zpmaginpscirms': model.zpmaginpscirms,
        #                   'clrcoeff': model.clrcoeff,
        #                   'clrcoeffunc': model.clrcoeffunc,
        #                   'ncalmatches': model.ncalmatches,
        #                   'exptime': model.exptime,
        #                   'adpctdif1': model.adpctdif1,
        #                   'adpctdif2': model.adpctdif2,
        #                   'diffmaglim': model.diffmaglim,
        #                   'zpdiff': model.zpdiff,
        #                   'programid': model.programid,
        #                   'jd': model.jd,
        #                   'rfid': model.rfid,
        #                   'forcediffimflux': model.forcediffimflux,
        #                   'forcediffimfluxunc': model.forcediffimfluxunc,
        #                   'forcediffimsnr': model.forcediffimsnr,
        #                   'forcediffimchisq': model.forcediffimchisq,
        #                   'forcediffimfluxap': model.forcediffimfluxap,
        #                   'forcediffimfluxuncap': model.forcediffimfluxuncap,
        #                   'forcediffimsnrap': model.forcediffimsnrap,
        #                   'aperturecorr': model.aperturecorr,
        #                   'dnearestrefsrc': model.dnearestrefsrc,
        #                   'nearestrefmag': model.nearestrefmag,
        #                   'nearestrefmagunc': model.nearestrefmagunc,
        #                   'nearestrefchi': model.nearestrefchi,
        #                   'nearestrefsharp': model.nearestrefsharp,
        #                   'refjdstart': model.refjdstart,
        #                   'refjdend': model.refjdend,
        #                   'procstatus': model.procstatus})
        # context = {}
        # render(request, template_name, context)
        return messages.success(request, f'SUCCESSFULLY UPLOADED {uploaded_file_path}')
