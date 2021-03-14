from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from google.cloud import storage

def mainView(request):
    if request.method =='POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        # client = storage.Client()
        # bucket = client.get_bucket('waitlist_input')
        # blob = bucket.blob(uploaded_file.name)
        # blob.upload_from_filename(uploaded_file.name)
    return render(request,'main.html')

def upload(request):
    return render(request,'upload.html')