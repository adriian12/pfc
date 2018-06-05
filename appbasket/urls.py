from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^equipos/$', views.equipos, name='equipos'),
    url(r'^precios/$', views.precios, name='precios'),
    url(r'^resultados/$', views.resultados, name='resultados'),
    url(r'^noticias/$', views.noticia_list, name='noticias'),
    url(r'^slider/$', views.slider_content, name='slider'),
    url(r'^columnas/$', views.columna_list, name='columnas'),
]