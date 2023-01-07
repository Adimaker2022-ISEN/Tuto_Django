from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from page_web import views

 

urlpatterns = [
    path("", include("page_web.urls")),
    path('admin/', admin.site.urls),
    re_path('', views.error404 )
]


urlpatterns += staticfiles_urlpatterns()