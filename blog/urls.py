"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import *
from django.conf.urls.static import static
from django.conf import settings

 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include('post.urls')),
    url(r'^makale/', include('home.urls')),
    url(r'^$', home_view, name = 'home'),
   #  url(r'^makale$', makale_view, name= 'makale'),
    url(r'^hakkimizda$', hakkimizda_view, name= 'hakkimizda'),
    url(r'^ekibimiz$', ekibimiz_view, name= 'ekibimiz'),
    url(r'^bvmb$', bvmb_view, name= 'bvmb'),
    url(r'^odemebilgileri$', odemebilgileri_view, name= 'odemebilgileri'),
    url(r'^sosyalsorumluluk$', sosyalsorumluluk_view, name= 'sosyalsorumluluk'),
    url(r'^faaliyetalanlarimiz$', faaliyetalanlarimiz_view, name= 'faaliyetalanlarimiz'),
    url(r'^bizeulasin$', bizeulasin_view, name= 'bizeulasin'),
    url(r'^kariyer$', kariyer_view, name= 'kariyer'),
    url(r'^bursbasvurusu$', bursbasvurusu_view, name= 'bursbasvurusu'),
    url(r'^vekaletbilgileri$', vekaletbilgileri_view, name= 'vekaletbilgileri'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)