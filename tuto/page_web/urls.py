from django.urls import path, re_path
from page_web import views

urlpatterns = [
    path("", views.home, name="home"),
    path('page2', views.page2, name='page2'),
]