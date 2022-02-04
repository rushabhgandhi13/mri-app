from django.shortcuts import render

def home(request):
    context = {
        
    }
    return render(request, 'segmi/index.html', context)

def labs(request):
    return render(request, 'segmi/lab.html')

def segment(request):
    return render(request, 'segmi/segment.html')

def myreport(request):
    return render(request, 'segmi/myreport.html')

def login1(request):
    return render(request, 'segmi/login.html')
