from django.shortcuts import render

# Create your views here.
def job(request):
    return render(request, 'job.html')