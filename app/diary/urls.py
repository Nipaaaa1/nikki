from django.urls import path

from diary import views

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("entry/", views.entry_list_view, name="entry_list_view"),

]
