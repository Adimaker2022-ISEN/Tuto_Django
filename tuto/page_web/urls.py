from django.urls import path
from page_web import views

urlpatterns = [
    path("", views.home, name="home"),
]