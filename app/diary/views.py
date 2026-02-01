from django.shortcuts import render

def hello_diary(request):
    return render(request, "diary/home.html") 
