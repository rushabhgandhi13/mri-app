
import numpy as np
from django.shortcuts import redirect, render
from django.contrib import messages
from mriapp.settings import MEDIA_ROOT, MEDIA_URL
from segmi.forms import *
from users.models import Profile
from .models import lab_report as doctorReport
from .models import appointment as apl
from django.views.decorators.csrf import csrf_exempt
from segmi.utils import *

set_seed(42)

model = load_model()

checkpoint_filepath = './model_checkpoint/'
model.load_weights(checkpoint_filepath)


def home(request):
   
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            I=form.save(commit=False)
            prf= Profile.objects.get(user=request.user)
            I.patient=prf
            I.save()
            messages.success(request, f'Appointment booked successfully!')
            return redirect(home)
    else:
        form = AppointmentForm()
    
    try:
        adm= False
        prf= Profile.objects.get(user=request.user)
        cat = prf.category
        if(request.user.is_superuser):
            adm = True
       
    except:
        cat = 'None'
    return render(request, 'segmi/index.html', {'form':form, 'cat':cat , 'adm':adm})



def doctor(request, id):
    rep = doctorReport.objects.get(id=id)
    img = rep.segment_img
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=rep)
        if form.is_valid():

            form.save()
            messages.success(request, f'Report submitted successfully!')
            return redirect('labreports')
    else:
        form = ReportForm(instance=rep)
    return render(request, 'segmi/doctorReport.html', {'form': form , 'id':id,'img':img})


def lab(request):
    if request.method == 'POST':
        form = LabReportForm(request.POST, request.FILES)
        if form.is_valid():
            instance= form.save(commit= False)
            volume = instance.report_img
            volume = np.load(volume, allow_pickle=False)
            raw_input = np.asarray(volume).astype("float32")
            output = predict(model, raw_input)
            output_slice = argmax_output(output, slice_num=64)
            plot_save_slice(raw_input, output_slice,path=os.path.join(MEDIA_ROOT,"test.png"),plot=False )
            instance.segment_img= "test.png"
            instance.save()
            messages.success(request, f'Report submitted successfully!')
            return redirect('lab')
    else:
        form = LabReportForm()
    return render(request, 'segmi/lab.html', {'form': form})





def labreports(request):

    prf= Profile.objects.get(user=request.user)

    context = {
        'report': lab_report.objects.filter(doctor=prf,Mark_as_seen=False),
        'report_seen': lab_report.objects.filter(doctor=prf,Mark_as_seen=True)
    }
    return render(request, 'segmi/labreports.html', context)


def myreport(request):
    prf= Profile.objects.get(user=request.user)
    context = {
        'report': lab_report.objects.filter(patient=prf,Mark_as_seen=True)
    }
    return render(request, 'segmi/myreport.html',context)

def aplist(request):

    context = {
        'unseen': apl.objects.filter(seen=False),
        'seen': apl.objects.filter(seen=True)
    }
    return render(request, 'segmi/aplist.html',context)


def patientReport(request, id):
    rep = doctorReport.objects.get(id=id)
    prf= Profile.objects.get(user=request.user)
    return render(request, 'segmi/patientReport.html', { 'id':id,'rep':rep,'prf':prf})

def appointment(request, id):
    rep = apl.objects.get(id=id)
    if request.method == 'POST':
        form = Apform(request.POST, instance=rep)
        if form.is_valid():

            form.save()
            messages.success(request, f'Report submitted successfully!')
            return redirect('aplist')
    else:
        form = Apform(instance=rep)

    return render(request, 'segmi/appointment.html', { 'id':id,'rep':rep,'form': form})
