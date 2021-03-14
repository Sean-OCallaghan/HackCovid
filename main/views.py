from os import read
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from google.cloud import storage
import pandas as pd
from django_project import read
import os

def mainView(request):
    if request.method =='POST':
        uploaded_file = request.FILES['document']
        input = pd.read_csv(uploaded_file)
        output = pd.DataFrame(input).to_csv('input.csv')

        client = storage.Client()
        bucket = client.get_bucket('waitlist_input')
        blob = bucket.blob('input.csv')
        blob.upload_from_filename('input.csv')

        read.func()

        blobs = bucket.list_blobs()
        for blob in blobs:
            blob.delete()

        new_csv = pd.read_csv('newWaitlist.csv')
        data_html = new_csv.to_html()
        
        if os.path.exists('input.csv'): os.remove('input.csv')
        if os.path.exists('newWaitlist.csv'): os.remove('newWaitlist.csv')

        return HttpResponse(data_html)

    return render(request,'main.html')

def upload(request):
    return render(request,'upload.html')