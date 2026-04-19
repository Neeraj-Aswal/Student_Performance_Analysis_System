from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def choice(request):
    return render(request, 'choice.html')