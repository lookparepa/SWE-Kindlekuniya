from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

def index(request):
    context = {
    }
    return render(request, 'index.html', context)
