#coding:utf-8
from django.shortcuts import render

  # Create your views here.
from django.http import HttpResponse
def index(request):
	return HttpResponse("Hello world, you are at")

def time(request):
	return HttpResponse("time")

def text(request):
	return render(request,'index.html')

def count(request):
	
	total_count = len(request.GET['text'])
	return render(request, 'count.html', {'count':total_count})
