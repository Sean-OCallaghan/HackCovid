from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import UploadFileForm


def mainView(request):
    return render(request,'main.html')