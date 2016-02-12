from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'blog/index.html', {})
def pantalla(request):
    return render(request, 'blog/pantalla.html', {})