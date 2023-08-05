from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'menu/home.html')

def about(request):
    return render(request, 'menu/about.html')
def aidata(request):
    return render(request, 'menu/ai.html')
