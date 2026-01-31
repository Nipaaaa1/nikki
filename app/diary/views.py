from django.http import HttpResponse
from django.shortcuts import render

def hello_diary(request):
    return HttpResponse(content="Hello Diary!")
