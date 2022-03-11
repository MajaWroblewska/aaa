# formularze do modeli
from django import forms
from django.forms import Textarea

from sklepApp.models import Kategoria, Produkt

#---------------------------------KATEGORIA--------------------------------
class KategoriaForm(forms.ModelForm):
    class Meta:
        model = Kategoria
        fields = '__all__'
    nazwa = forms.CharField(max_length=100)








#---------------------------------PRODUKT----------------------------------
class ProduktForm(forms.ModelForm):
    class Meta:
        model= Produkt
        # fields= '__all__'
        exclude= ['data_dodania','data_modyfikacji','nazwa' ]

    nazwa = forms.CharField(max_length=200)
    kategoria = forms.ModelChoiceField(queryset=Kategoria.objects)
    opis = forms.CharField(widget=Textarea)
    zdjecie = forms.ImageField()
    ilosc_w_magazynie = forms.IntegerField(min_value=0,)
    cena = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2)
    data_dodania = forms.DateTimeField()
    data_modyfikacji = forms.DateTimeField()


class ProduktSelectForm(forms.Form):
    produkty= forms.ModelChoiceField(queryset=Produkt.objects)

#---------------------------------EMAIL------------------------------------

#---------------------------------ADRES------------------------------------

#---------------------------------USER-------------------------------------

#---------------------------------KOSZYK_LOGIN-----------------------------

#---------------------------------KOSZYK_LOGOUT----------------------------
