from django.db import models

# Create your models here.
class Kategoria(models.Model):
    nazwa= models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nazwa}'

#-------------------------------------------------------------------------------
class Produkt(models.Model):
    nazwa= models.CharField(max_length=200)
    kategoria_id= models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    opis= models.TextField()
    zdjecie= models.ImageField(upload_to ='uploads/', default='abc', null=True)
    ilosc_w_magazynie= models.IntegerField(default=0)
    cena= models.DecimalField(max_digits=7, decimal_places=2, default=1.00)
    data_dodania= models.DateTimeField(auto_now_add=True)
    data_modyfikacji= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nazwa}-kat= {self.kategoria_id}- cena= {self.cena} -stan={self.ilosc_w_magazynie} {self.zdjecie} -{self.data_dodania}/{self.data_modyfikacji}'
#-------------------------------------------------------------------------------

class Email(models.Model):
    mail= models.EmailField()

    def __str__(self):
        return f'{self.mail}'
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
    email_id= models.ForeignKey(Email, on_delete=models.CASCADE)
    adres_id= models.ForeignKey(Adres, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.imie} {self.nazwisko} - {self.login}'
# -------------------------------------------------------------------------------
class Koszyk_login(models.Model):
    nr_zamowienia= models.IntegerField()
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
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
