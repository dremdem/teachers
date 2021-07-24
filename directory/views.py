from django.shortcuts import render

from directory.models import Teacher

# Create your views here.

def index(request):
    context = {"teachers": Teacher.objects.all()}
    return render(request, 'index.html', context=context)
