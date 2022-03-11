from django.db import models
from django.utils import timezone

# Create your models here.


class Kategoria(models.Model):
    nazwa= models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nazwa}'

#-------------------------------------------------------------------------------
class Produkt(models.Model):
    nazwa= models.CharField(max_length=200)
    kategoria= models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    opis= models.TextField(default='opis_domyślny')
    zdjecie= models.ImageField(upload_to ='moja_sciezka/', default='domyslna_sciezka', null=True)
    ilosc_w_magazynie= models.IntegerField(default=0)
    cena= models.DecimalField(max_digits=7, decimal_places=2, default=1.00)
    data_dodania= models.DateTimeField(auto_now_add=True) #podczas tworzenia
    data_modyfikacji= models.DateTimeField(auto_now=True) #przy zapisie

    def __str__(self):
        return f'{self.nazwa} : img={self.zdjecie} : stan={self.ilosc_w_magazynie} : cena= {self.cena}'# : data dod/mod= {self.data_dodania}/{self.data_modyfikacji}'
#-------------------------------------------------------------------------------

class Email(models.Model):
    email= models.EmailField()

    def __str__(self):
        return f'{self.email}'
#-------------------------------------------------------------------------------

class Adres(models.Model):
    kraj= models.CharField(max_length=100)
    miasto= models.CharField(max_length=100)
    ulica= models.CharField(max_length=100)
    nr_budynku= models.IntegerField()
    nr_mieszkania= models.IntegerField()

    def __str__(self):
        return f'{self.id}'
# -------------------------------------------------------------------------------
class User(models.Model):
    imie= models.CharField(max_length=100)
    nazwisko= models.CharField(max_length=200)
    login= models.CharField(max_length=100)
    email= models.ForeignKey(Email, on_delete=models.CASCADE)
    adres= models.ForeignKey(Adres, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.imie} {self.nazwisko} - {self.login}'
# -------------------------------------------------------------------------------
class Koszyk_login(models.Model):
    nr_zamowienia= models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    produkt= models.ManyToManyField(Produkt)

    def __str__(self):
        return f'{self.nr_zamowienia}'
# -------------------------------------------------------------------------------

class Koszyk_logout(models.Model):
    nr_zamowienia= models.IntegerField()
    produkt= models.ManyToManyField(Produkt)

    def __str__(self):
        return f'{self.nr_zamowienia}'
# -------------------------------------------------------------------------------
