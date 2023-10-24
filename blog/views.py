from django.shortcuts import render

def minha_view(request):
    return render(request, 'templates/blog/index.html')

# Create your views here.
