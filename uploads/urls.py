from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.stronaglowna, name='stronaglowna'),
    url('autobusy/', views.autobusy, name='autobusy'),
    url('trawmaje/', views.tramwaje, name='tramwaje'),
    url('jf/',views.jf,name="jf"),
    url('od/',views.od,name="od"),
    url('wg/',views.wg,name="wg"),
    url('sp/',views.sp,name="sp"),
    url('gs/',views.gs,name="gs"),
    url('jm/',views.jm,name="jm"),
    url('AS/',views.AS,name="AS"),
    url('GO/',views.GO,name="GO"),
    url('BK/',views.BK,name="BK"),
    url('GSCH/',views.GSCH,name="GSCH"),
    url('PP/',views.PP,name="PP"),
    url('SG/',views.SG,name="SG")

]
