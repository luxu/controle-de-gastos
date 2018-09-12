# coding: utf-8

from website.models import Comercio

def comercios(request):
    return {
        'comercios' : Comercio.objetos.all()
    }
