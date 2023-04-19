from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #print("request:::", request.META)
    #print("request:::", request.HEADERS)
    context = dict()
    return render(request, 'page/index.html', context)

def about_us(request):
    context = dict()
    return render(request, "page/about.html", context)

def contact(request):
    context = dict()
    return render(request, "page/contact.html", context)

def vision(request):
    context = dict()
    return render(request, "page/vision.html", context)

# def aghamir(request):
#     context = dict()
#     return HttpResponse('Agamir Agamirli.')