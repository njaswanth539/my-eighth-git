from django.urls import path
from app1.views import *
app_name='jasu'

urlpatterns=[ 
    path('first/',first,name='first'),
]