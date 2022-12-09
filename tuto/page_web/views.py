from django.shortcuts import render


def home (request):
    return render(request, 'page_web/index.html')
