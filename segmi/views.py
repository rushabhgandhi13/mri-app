from django.shortcuts import redirect, render
from django.contrib import messages
from segmi.forms import *

def home(request):
    context = {
        
    }
    return render(request, 'segmi/index.html', context)

def labs(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, f'Report submitted successfully!')
            return redirect('lab')
    else:
        form = ReportForm()
    return render(request, 'segmi/lab.html', {'form': form})

def segment(request):
    return render(request, 'segmi/segment.html')

def myreport(request):
    return render(request, 'segmi/myreport.html')

