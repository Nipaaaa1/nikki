from django.shortcuts import render

from diary.models import Home, Diary

def home_view(request):
    home = Home.objects.first()
    diaries = Diary.objects.order_by("-created")[:2]

    return render(
        request, 
        "diary/home.html", 
        {
            "home": home,
            "diaries": diaries
        }
    )

def entry_list_view(request):
    diaries = Diary.objects.order_by("-created")

    return render(
        request,
        "diary/entry_list.html",
        {
            "diaries": diaries
        }
    )

