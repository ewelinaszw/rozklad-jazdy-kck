from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.stronaglowna, name='stronaglowna'),
    url('rozklad/', views.rozklad, name='rozklad'),
    url('trawmaje/', views.tramwaje, name='tramwaje'),
    url('jf/',views.jf,name="jf"),
    url('od/',views.od,name="od"),
    url('wg/',views.wg,name="wg"),
    url('sp/',views.sp,name="sp"),
    url('gs/',views.gs,name="gs"),
    url('jm/',views.jm,name="jm"),


]
