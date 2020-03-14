from django.urls import path
from .views import *

urlpatterns = [
    path('script', Script.as_view(), name='script'),
    path('analyse', Analyse.as_view(), name='analyse')
]