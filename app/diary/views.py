from django.shortcuts import render

from diary.models import Home, Diary

def home_view(request):
    home = Home.objects.first()
    diaries = Diary.objects.order_by("-created").values("id", "title", "created")[:2]

    return render(
        request, 
        "diary/home.html", 
        {
            "home": home,
            "diaries": diaries
        }
    )

def entry_list_view(request):
    diaries = Diary.objects.order_by("-created").values("id", "title", "created")

    return render(
        request,
        "diary/entry_list.html",
        {
            "diaries": diaries
        }
    )

def entry_detail_view(request, entry_id):
    diary = Diary.objects.filter(id__exact=entry_id).first()

    return render(
        request,
        "diary/entry_detail.html",
        {
            "diary": diary
        }
    )


