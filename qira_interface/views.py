from django.shortcuts import render
from django.conf import settings
import os

# Create your views here.
def index(request):

    context = {
        'qv': settings.VERSION,
        'visited': visits,
    }
    
    return render(request,'qira_interface/index.html',context)
    