from .models import Comercio, Gasto
from django import forms
from django.contrib.admin import widgets
# from dal import autocomplete


# FORMULÁRIO DE INCLUSÃO DE GASTOS
# -------------------------------------------

class InsereGastoForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    datagasto = forms.DateField(widget=widgets.AdminDateWidget)


    class Meta:
        # Modelo base
        model = Gasto

        # Campos que estarão no form
        fields = [
            'name',
            'slug',
            'valor',
            'datagasto',
            'comercio'
        ]


# FORMULÁRIO DE INCLUSÃO DE COMÉRCIOS
# -------------------------------------------

class InsereComercioForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Comercio

        # Campos que estarão no form
        fields = [
            'name',
            'slug'
        ]
