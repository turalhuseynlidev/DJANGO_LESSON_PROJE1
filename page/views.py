from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #print("request:::", request.META)
    #print("request:::", request.HEADERS)
    return render(request, 'page/homepage.html', {})