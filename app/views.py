from django.http.response import HttpResponse

import random

def hello_view(request, name):

    return HttpResponse(f"Hello {name}")

def roll_die_view(request, sides):
    roll = random.randint(1,sides)
    return HttpResponse(roll)

def random_between_view(request, lo, hi):
    return HttpResponse(random.randint(lo,hi))

def hey(request,name):
    return HttpResponse(f"Hey, {name}!")

def how_old(request,end,birthyear):
    return HttpResponse(end - birthyear)

def good_burger(request,burgers,fries,drinks):
    return HttpResponse((burgers * 4.5) + (fries * 1.5) + drinks)