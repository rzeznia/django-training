from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
import datetime


# Create your views here.



def welcome(request):
    return HttpResponse('Witaj świecie')


def warning(request):
    return render(request, "hello_world/warning.html")


def about(request):
    return render(request, "hello_world/about.html")


def time_of_death(request):
    persons = Person.objects.order_by("-mass")[:5]
    #text = person.name +  " umrzesz dokladnie o "
    #godzina = datetime.datetime.now() + datetime.timedelta(days=10)
    context = {"time_of_death": persons}
    return render(request, "hello_world/death.html", context)

def cal_calculator(request):
    persons = Person.objects.order_by("-mass")[:5]
    for i in persons:
         i.cal = i.cal_cal()
    context = {"cal_calculator": persons}
    return render(request, "hello_world/cal.html", context)


#About -> Nasze imiona
#Kiedy_Śmierć -> now() + 10 dni;
#import datetime