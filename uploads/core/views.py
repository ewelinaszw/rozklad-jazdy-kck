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
def fj(request):
    print('1-Franowo-Junikowo')
    return render(request, 'fj.html')
def od(request):
    print('2-Ogrody-Dębiec')
    return render(request, 'od.html')
def do(request):
    print('2-Dębiec-Ogrody')
    return render (request, 'do.html')
def gw(request):
    print('3-Górczyn-Wilczak')
    return render (request, 'gw.html')
def wg(request):
    print('3-Wilczak-Górczyn')
    return render (request, 'wg.html')
def sp(request):
    print('4-Starołęka-Połabska')
    return render (request, 'sp.html')
def ps(request):
    print('4-Połabska-Starołęka')
    return render (request, 'sp.html')
