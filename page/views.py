from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #print("request:::", request.META)
    #print("request:::", request.HEADERS)
    context = dict()
    return render(request, 'page/index.html', context)

def about_us(request):
    title = 'About Us'
    context = dict(
        page_title=title,
        )
    return render(request, "page/about.html", context)

def contact(request):
    title = 'Contact with Us'
    context = dict(
        page_title=title,
        )
    return render(request, "page/contact.html", context)

def vision(request):
    title = 'Our Vision'
    context = dict(
        page_title=title,
        )
    return render(request, "page/vision.html", context)

# def aghamir(request):
#     context = dict()
#     return HttpResponse('Agamir Agamirli.')