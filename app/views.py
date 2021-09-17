from django.http.response import HttpResponse
from django.http.request import HttpRequest 
from django.shortcuts import render
from django.http import request

def hey(request: HttpRequest, name) -> HttpResponse:
    return HttpResponse(f"Hello, {name}!")


def how_old(request: HttpRequest, end, birthyear) -> HttpResponse:
    return HttpResponse(end - birthyear)


def good_burger(request: HttpRequest, burgers, fries, drinks) -> HttpResponse:
    return HttpResponse((burgers * 4.5) + (fries * 1.5) + drinks)