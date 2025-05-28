from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def sobre(request):
    return render(request, 'home/sobre.html')