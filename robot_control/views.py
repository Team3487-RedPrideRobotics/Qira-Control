from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):

    context = {
        'qv': settings.VERSION
    }

    return render(request, 'robot_control/index.html', context)