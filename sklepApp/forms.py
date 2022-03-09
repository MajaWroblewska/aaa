# formularze do modeli
from django import forms
from django.forms import Textarea

from sklepApp.models import Kategoria, Produkt


class KategoriaForm(forms.Form):
    nazwa= forms.CharField(max_length=100)


class ProduktForm(forms.ModelForm):
    class Meta:
        model= Produkt
        # fields= '__all__'
        exclude= ['data_dodania','data_modyfikacji', ]

    nazwa = forms.CharField(max_length=200)
    kategoria = forms.ModelChoiceField(queryset=Kategoria.objects)
    # opis = forms.CharField(default='opis_domyślny')
    opis = forms.CharField(widget=Textarea)
    # zdjecie = forms.ImageField()
    ilosc_w_magazynie = forms.IntegerField(min_value=0,)
    cena = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2)
    # data_dodania = forms.DateTimeField()
    # data_modyfikacji = forms.DateTimeField()


