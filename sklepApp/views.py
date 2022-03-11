from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, FormView, UpdateView, DeleteView

# Create your views here.
from sklepApp.models import Produkt
from sklepApp.forms import ProduktForm, ProduktSelectForm
# from sklepApp.models import Kategoria

#---------------------------------LOGOWANIE--------------------------------
class MojeLogwanie(LoginView):
    template_name = 'login.html'


# ---------------------------------KATEGORIA--------------------------------
from sklepApp.models import Kategoria
from sklepApp.forms import KategoriaForm


class KategoriaView(View):
    def get(self, request):
        return render(request,
                      template_name='kategoria.html',
                      context={'kategorie': Kategoria.objects.all()})


class KategoriaCreateView(FormView):
    template_name = 'kategoria_form.html'
    form_class = KategoriaForm
    success_url = reverse_lazy('kategoria')

    def form_valid(self, form):
        result = super(KategoriaCreateView, self).form_valid(form)

        moje_kategorie = form.cleaned_data
        Kategoria.objects.create(
                                 nazwa = moje_kategorie['nazwa'],
                                 )
        return result


class KategoriaUpdateView(UpdateView):
    template_name = 'kategoria_form.html'
    model = Kategoria
    form_class = KategoriaForm
    success_url = reverse_lazy('kategoria')


class KategoriaDeleteView(DeleteView):
    template_name = 'kategoria_delete_form.html'
    model = Kategoria
    success_url = reverse_lazy('kategoria')


#---------------------------------PRODUKT----------------------------------
class ProduktView(View):
    def get(self,request):
        return render(request,
                      template_name='produkt.html',
                      context={'produkty': Produkt.objects.all()},
                      )

# class ProduktCreateView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
class ProduktCreateView(LoginRequiredMixin, FormView):
    template_name = 'produkt_form.html'
    form_class = ProduktForm
    success_url = reverse_lazy('produkt')
    # permission_required = 'sklepApp.add_produkt'

    def form_valid(self, form):
        result= super().form_valid(form)
        moj_produkt=form.cleaned_data
        Produkt.objects.create(nazwa= moj_produkt['nazwa'],
                               kategoria= moj_produkt['kategoria'],
                               opis= moj_produkt['opis'],
                               # zdjecie=moj_produkt['zdjecie'],
                               ilosc_w_magazynie=moj_produkt['ilosc_w_magazynie'],
                               cena=moj_produkt['cena'],
                               data_dodania=moj_produkt['data_dodania'],
                               data_modyfikacji=moj_produkt['data_modyfikacji']
                               )
        return result

# class ProduktUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
class ProduktUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'produkt_form.html'
    model = Produkt
    form_class = ProduktForm
    success_url = reverse_lazy('produkt')
    permission_required = 'sklepApp.change_produkt'


# class ProduktSelectUpdateView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
class ProduktSelectUpdateView(LoginRequiredMixin, FormView):
    template_name = 'produkt_select_form.html'
    form_class = ProduktSelectForm
    success_url = reverse_lazy('produkt')
    permission_required = 'sklepApp.change_produkt'


    def form_valid(self, form):
        result = super().form_valid(form)

        moje_produkty = form.cleaned_data   #to dict o key='produkt1' z klasy formularza
        id_produkt = moje_produkty['produkty'].id
        # print(id_produkt)

        response = redirect('produkt_update', pk=id_produkt)    #przekierowanie do name url i przekazanie zmiennek <pk>
        return response


# class ProduktDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
class ProduktDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'produkt_delete_form.html'
    model = Produkt
    success_url = reverse_lazy('produkt')
    permission_required = 'slepApp.delete_produkt'


# class ProduktSelectDeleteView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
class ProduktSelectDeleteView(LoginRequiredMixin, FormView):
    template_name = 'produkt_select_form.html'
    form_class = ProduktSelectForm
    success_url = reverse_lazy('produkt')
    permission_required = 'sklepApp.delete_produkt'

    def form_valid(self, form):
        # result= super().form_valid(form) #! poniżej ok !
        result= super(ProduktSelectDeleteView, self).form_valid(form)
        moje_produkty = form.cleaned_data

        id_produkt = moje_produkty['produkty'].id
        odp = redirect('produkt_delete', pk=id_produkt)

        return odp

#---------------------------------EMAIL------------------------------------

#---------------------------------ADRES------------------------------------

#---------------------------------USER-------------------------------------

#---------------------------------KOSZYK_LOGIN-----------------------------

#---------------------------------KOSZYK_LOGOUT----------------------------

#--------------------------------------------------------------------------
#autoryzacja (Produkt, Kategoria, Email, Adres, User, Koszyk_login, Koszyk_logout, ) -

# ( Email, Adres, User, Koszyk_login, Koszyk_logout), + widok
# ( Email, Adres, User, Koszyk_login, Koszyk_logout), + formularz
# ( Email, Adres, User, Koszyk_login, Koszyk_logout), + update i delete
# (Kategoria, Email, Adres, User, Koszyk_login, Koszyk_logout), + select do update i delete
# (Kategoria, Email, Adres, User, Koszyk_login, Koszyk_logout), + autentykacja
