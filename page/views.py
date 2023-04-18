from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #print("request:::", request.META)
    #print("request:::", request.HEADERS)
    context = dict()
    return render(request, 'page/homepage.html', context)

def about_us(request):
    context = dict()
    return render(request, "page/about_us.html", context)

def contact(request):
    context = dict()
    return render(request, "page/contact.html", context)

# def aghamir(request):
#     context = dict()
#     return HttpResponse('Agamir Agamirli.')