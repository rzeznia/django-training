from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def welcome(request):
    return HttpResponse('Witaj świecie');


def warning(request):
    return HttpResponse("JEST KORONA! NIE MA PAPIRU!")


def about(request):
    return HttpResponse(
        """
        <h2>Autorzy</h2>
        <ul><li>Marcin Rzeźnik</li><li>Karol Sobisz</li></ul>
        """
    )


def death(request):
    return HttpResponse(datetime.datetime.now() + datetime.timedelta(days=10))


#About -> Nasze imiona
#Kiedy_Śmierć -> now() + 10 dni;
#import datetime