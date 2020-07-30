from __future__ import print_function, unicode_literals
from django.shortcuts import render,HttpResponse
from . forms import ImageUploadForm
from . models import content
import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd


# Create your views here.
def home(request):
    context = {'form':ImageUploadForm()}
    return render(request,'home.html',context)

def allcontents(request):
    allcontents = content.objects.all()
    context = {'allcontents':allcontents}
    return render(request,"contents.html",context)    

def searchfromtext(request):
    searchquery = request.GET['search']
    allposts = content.objects.filter(title__icontains=searchquery)
    context = {'allposts':allposts}
    return render(request,'searchpage.html',context)


def searchfromimage(request):
    image_file = request.FILES['file']
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'YourGoogleServiceAccountToken.json'
    client = vision.ImageAnnotatorClient()
    yo = image_file.read()
    image = vision.types.Image(content=yo)
    response = client.document_text_detection(image=image)
    docText = response.full_text_annotation.text
    docText.replace('\n',' ')
    searchquery = docText.strip()
    print(searchquery)
    allposts = content.objects.filter(title__icontains=searchquery)
    context = {'allposts':allposts}
    return render(request,'searchpage.html',context)

