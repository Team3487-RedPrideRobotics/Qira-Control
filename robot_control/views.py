from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Congrats! You are now viewing QIRA 0.0.1", content_type='text/plain')