from django.contrib import admin
from sklepApp.models import Kategoria, Produkt
from sklepApp.models import Email, Adres, User
from sklepApp.models import Koszyk_login, Koszyk_logout

# Register your models here.
admin.site.register(Kategoria)
admin.site.register(Produkt)
admin.site.register(Email)
admin.site.register(Adres)
admin.site.register(User)
admin.site.register(Koszyk_login)
admin.site.register(Koszyk_logout)