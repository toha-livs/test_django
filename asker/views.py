from django.shortcuts import render
from django.http import HttpResponse

def index (reqest):
    return HttpResponse("<h3>привет Мир!<h3>")

