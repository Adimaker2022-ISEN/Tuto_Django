from django.shortcuts import render


def home (request):
    return render(request, 'page_web/index.html')

def page2 (request):
    return render(request, 'page_web/page2.html')

def error404(request):
    return render(request, 'page_web/vue404.html')
