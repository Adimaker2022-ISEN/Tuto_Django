from django.urls import path
from apptuto import views

urlpatterns = [
    path("", views.home, name="home"),
]