from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
import datetime
# Create your views here.
def welcome(request):
    return HttpResponse('Witaj świecie');


def warning(request):
    return render(request, "hello_world/warning.html")


def about(request):
    return render(request, "hello_world/about.html")


def death(request):
    person = Person.objects.get(pk=1)
    persons = Person.objects.order_by("-mass")[:5]
    godzina = datetime.datetime.now() + datetime.timedelta(days=10)
    temp_dict = {"time_of_death":person}
    return render(request, 'hello_world/death.html', temp_dict)


#About -> Nasze imiona
#Kiedy_Śmierć -> now() + 10 dni;
#import datetime