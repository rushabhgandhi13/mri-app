from django.shortcuts import redirect, render
from django.contrib import messages
from segmi.forms import *
from .models import lab_report as doctorReport
def home(request):
    context = {
        
    }
    return render(request, 'segmi/index.html', context)

def doctor(request):
    if request.method == 'POST':
        form = ReportForm(request.POST,request.FILES)
        if form.is_valid() :
            form.save()
            messages.success(request, f'Report submitted successfully!')
            return redirect('lab')
    else:
        form = ReportForm()
    return render(request, 'segmi/doctorReport.html', {'form': form})

def doctor(request,id):
    rep = doctorReport.objects.get(id=id)
    if request.method == 'POST':
        form = ReportForm(request.POST,request.FILES,instance=rep)
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
        if form.is_valid() :
            form.save()
            messages.success(request, f'Report submitted successfully!')
            return redirect('lab')
    else:
        form = LabReportForm()
    return render(request, 'segmi/lab.html', {'form': form})

def segment(request):
    return render(request, 'segmi/segment.html')

def labreports(request):
    context={
        'report':lab_report.objects.all()
    }
    return render(request, 'segmi/labreports.html',context)

def myreport(request):
    return render(request, 'segmi/myreport.html')

