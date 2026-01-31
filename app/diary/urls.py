from django.urls import path

from diary import views

urlpatterns = [
    path("", views.hello_diary, name="hello_diary"),
]
