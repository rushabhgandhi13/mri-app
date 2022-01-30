from django.shortcuts import render

def home(request):
    context = {
        
    }
    return render(request, 'segmi/index.html', context)
