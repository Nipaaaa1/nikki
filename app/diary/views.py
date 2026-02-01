from django.shortcuts import render

from diary.models import Home, Diary

def hello_diary(request):
    home = Home.objects.first()
    diaries = Diary.objects.all()

    return render(
        request, 
        "diary/home.html", 
        {
            "home": home,
            "diaries": diaries
        }) 
