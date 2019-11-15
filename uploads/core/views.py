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
