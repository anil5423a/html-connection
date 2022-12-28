from django.urls import path
from app2.views import *
app_name='something 2'

urlpatterns=[
    path('one1/',one1,name='one1'),
    path('two/',two,name='two'),
]