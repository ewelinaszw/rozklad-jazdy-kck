from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def stronaglowna(request):
    print('Strona główna')
    return render(request, 'stronaglowna.html')


def rozklad(request):
    print('Rozkład jazdy autobusów')
    return render(request, 'rozklad.html')


def tramwaje(request):
    print('Rozkład jazdy trwamwajów')
    return render(request, 'tramwaje.html')
def jf(request):
    print('1-Junikowo-Franowo')
    return render(request, 'jf.html')
def od(request):
    print('2-Ogrody-Dębiec')
    return render(request, 'od.html')
def wg(request):
    print('3-Wilczak-Górczyn')
    return render (request, 'wg.html')
def sp(request):
    print('4-Starołęka-Połabska')
    return render (request, 'sp.html')
def gs(request):
    print('5-Górczyn-Stomil')
    return render (request, 'gs.html')
def jm(request):
    print('6-Junikowo-Miłostowo')
    return render (request, 'jm.html')
