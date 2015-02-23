#!/usr/bin/env python
#coding: utf8 

from django import forms


class EntradaForm(forms.Form):
    entrada = forms.CharField(widget = forms.TextInput(), label='')
    entrada.widget.attrs.update({'placeholder' : 'Ingresar Numero', 'type':'text' , 'class':'form-control',})
