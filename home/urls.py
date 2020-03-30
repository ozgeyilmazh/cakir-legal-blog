from django.conf.urls import url
from .views import *

app_name = 'makale'
urlpatterns = [
    url(r'^index/$', makale_index, name= 'index'),
    #Dinamik URL ler
    url(r'^(?P<slug>[\w-]+)/$', makale_detail, name = 'detail'), 

    
]
