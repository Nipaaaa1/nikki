from django.urls import path

from diary import views

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("entry/", views.entry_list_view, name="entry_list_view"),
    path("entry/<int:entry_id>", views.entry_detail_view, name="entry_detail_view"),


]
