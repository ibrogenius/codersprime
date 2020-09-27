from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Pioneer


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def members(request):
    mem = Member.objects.all()
    pion = Pioneer.objects.all()
    return render(request, 'members.html', {'mem':mem, 'pion':pion})


def projects(request):
    return render(request, 'projects.html')


def gallery(request):
    return render(request, 'gallery.html')