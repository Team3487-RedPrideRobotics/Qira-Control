from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

# Create your views here.
def index(request):

    context = {
        'qv': settings.VERSION
    }

    return render(request, 'robot_control/index.html', context)

not_started = True
def face(request):

    global not_started
    if not_started:
        context = {
            'qv': settings.VERSION
        }
        not_started = False
        return render(request, 'robot_control/face/startup.html', context)
    
    context = {}

    return render(request, 'robot_control/face/face.html', context)

def get_js(request):
    data = {}
    return JsonResponse(data)