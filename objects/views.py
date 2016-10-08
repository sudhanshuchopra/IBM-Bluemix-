from django.shortcuts import render
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition
import json
from os.path import join, dirname
from os import environ
from .models import tags,visobjects
from django.http import HttpResponse,Http404
from.forms import searchform
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.models import Site

@require_http_methods(['GET','POST'])
def search(request):
	if(request.method=='POST'):
		f=searchform(request.POST,request.FILES)
		if not f.is_valid():
			return render(request,'objects/home.html',{'f':f})
		userobj=f.save(commit=False)	
		userobj.save()
		visual_recognition = VisualRecognition('2016-09-30',api_key='7a85ea3ccce43d03daea662cb7b6b7236aeb4dd0')
		img=visual_recognition.classify(images_url="http://127.0.0.1:8000/images/9/")
		print(json.dumps(img,indent=2))

		p=img.images.classifiers.classes
		for i in p:
			d=i['class']
			tags.objects.create(tags_value=d,parent=userobj)
		return HttpResponse('OK')

	if(request.method=='GET'):
		f=searchform()
		return render(request,'objects/home.html',{'f':f})
def show(request,id)	:
	v=visobjects.objects.get(pk=id)
	return render(request,'objects/show.html',{'v':v})