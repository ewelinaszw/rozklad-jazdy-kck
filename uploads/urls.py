from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.stronaglowna, name='stronaglowna'),
    url('rozklad/', views.rozklad, name='rozklad'),
    url('trawmaje/', views.tramwaje, name='tramwaje'),
    url('jf/',views.jf,name="jf"),
    url('fj/',views.fj,name="fj"),

]
