from django.urls import path
from app2.views import *
app_name='app2'

urlpatterns=[
    path('shwetha/',shwetha,name='shwetha'),
    path('soni/',soni,name='soni'),
]