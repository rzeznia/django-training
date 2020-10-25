from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def welcome(request):
    return HttpResponse('Witaj świecie');


def warning(request):
    return render(request, "hello_world/warning.html")


def about(request):
    return render(request, "hello_world/about.html")


def death(request):
    return HttpResponse(datetime.datetime.now() + datetime.timedelta(days=10))


#About -> Nasze imiona
#Kiedy_Śmierć -> now() + 10 dni;
#import datetime