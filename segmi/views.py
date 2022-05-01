import numpy as np
from django.shortcuts import redirect, render
from django.contrib import messages
from mriapp.settings import MEDIA_ROOT, MEDIA_URL
from segmi.forms import *
from .models import lab_report as doctorReport
from django.views.decorators.csrf import csrf_exempt
from segmi.utils import *

set_seed(42)

model = load_model()

checkpoint_filepath = './model_checkpoint/'
model.load_weights(checkpoint_filepath)


def home(request):
    context = {

    }
    return render(request, 'segmi/index.html', context)


def doctor(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Report submitted successfully!')
            return redirect('lab')
    else:
        form = ReportForm()
    return render(request, 'segmi/doctorReport.html', {'form': form})


def doctor(request, id):
    rep = doctorReport.objects.get(id=id)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=rep)
        if form.is_valid():

            form.save()
            messages.success(request, f'Report submitted successfully!')
            return redirect('labreports')
    else:
        form = ReportForm(instance=rep)
    return render(request, 'segmi/doctorReport.html', {'form': form})


def lab(request):
    if request.method == 'POST':
        form = LabReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Report submitted successfully!')
            return redirect('lab')
    else:
        form = LabReportForm()
    return render(request, 'segmi/lab.html', {'form': form})


def segment(request):
    if request.method == 'POST':
        form = LabReportsegmentForm(request.POST, request.FILES,instance=doctorReport.objects.get(id=1))
        if form.is_valid():
            instance= form.save(commit= False)
            volume = instance.segment_img
            volume = np.load(volume, allow_pickle=False)
            raw_input = np.asarray(volume).astype("float32")
            output = predict(model, raw_input)
            output_slice = argmax_output(output, slice_num=64)
            plot_save_slice(raw_input, output_slice,path=os.path.join(MEDIA_ROOT,"test.png") )
            instance.segment_img= "test.png"
            instance.save()
            messages.success(request, f'Segmentation done successfully!')
            return redirect('segment')
    else:
        form = LabReportsegmentForm(request.POST, request.FILES,instance=doctorReport.objects.get(id=1))

        
    return render(request, 'segmi/segment.html',{'form': form})


def labreports(request):
    context = {
        'report': lab_report.objects.all()
    }
    return render(request, 'segmi/labreports.html', context)


def myreport(request):
    return render(request, 'segmi/myreport.html')


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Appointment booked successfully!')
            return redirect('')
    else:
        form = AppointmentForm()
    return render(request, 'segmi/index.html', {'form': form})
