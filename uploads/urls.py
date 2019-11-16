from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.stronaglowna, name='stronaglowna'),
    url('rozklad/', views.rozklad, name='rozklad'),
    url('trawmaje/', views.tramwaje, name='tramwaje'),
    url('jf/',views.jf,name="jf"),
    url('fj/',views.fj,name="fj"),
    url('od/',views.od,name="od"),
    url('do/',views.do,name="do"),
    url('gw/',views.gw,name="gw"),
    url('wg/',views.wg,name="wg"),
    url('sp/',views.sp,name="sp"),
    url('ps/',views.ps,name="ps"),

]
