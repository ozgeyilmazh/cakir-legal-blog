from django.conf.urls import url
from .views import *

app_name = 'post'
urlpatterns = [
    url(r'^index/$', post_index, name= 'index'),
    #Dinamik URL ler
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name = 'detail'), 
    url('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    url('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    url('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    
]
