from django.shortcuts import render

from .models import Instrument


# Create your views here.

def home(request):
    # it = Instrument()
    # it.name = 'guitar'
    # it.price = 10000
    # it.desc = "The guitar is a fretted musical instrument that typically has six strings. It is usually held flat against the player's body"
    # it.img = 'guitar.jpg'

    instru = Instrument.objects.all()
    return render(request, 'index.html', {'aaa': instru})
