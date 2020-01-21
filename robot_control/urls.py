from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('qira-face', views.face, name='face'),
    path('qira_robot_data', views.get_js, name="get js")
]