from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, FormView, UpdateView, DeleteView

# Create your views here.
from sklepApp.models import Produkt
from sklepApp.forms import ProduktForm, ProduktSelectForm


#--------------------------------------------------------------------------
class MojeLogwanie(LoginView):
    template_name = 'login.html'

#--------------------------------------------------------------------------
class ProduktView(View):
    def get(self,request):
        return render(request,
                      template_name='produkt.html',
                      context={'produkty': Produkt.objects.all()},
                      )

class ProduktCreateView(LoginRequiredMixin, FormView):
    template_name = 'produkt_form.html'
    form_class = ProduktForm
    success_url = reverse_lazy('produkt_create')

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

class ProduktUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'produkt_form.html'
    model = Produkt
    form_class = ProduktForm
    success_url = reverse_lazy('produkt')


class ProduktSelectUpdateView(LoginRequiredMixin, FormView):
    template_name = 'produkt_select_form.html'
    form_class = ProduktSelectForm
    success_url = reverse_lazy('produkt')

    def form_valid(self, form):
        result = super().form_valid(form)

        moje_produkty = form.cleaned_data   #to dict o key='produkt1' z klasy formularza
        id_produkt = moje_produkty['produkty'].id
        # print(id_produkt)

        response = redirect('produkt_update', pk=id_produkt)    #przekierowanie do name url i przekazanie zmiennek <pk>
        return response


class ProduktDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'produkt_delete_form.html'
    model = Produkt
    success_url = reverse_lazy('produkt')

class ProduktSelectDeleteView(FormView):
    template_name = 'produkt_select_form.html'
    form_class = ProduktSelectForm
    success_url = reverse_lazy('produkt')

    def form_valid(self, form):
        # result= super().form_valid(form) #! poniżej ok !
        result= super(ProduktSelectDeleteView, self).form_valid(form)
        moje_produkty = form.cleaned_data

        id_produkt = moje_produkty['produkty'].id
        odp = redirect('produkt_delete', pk=id_produkt)

        return odp


#--------------------------------------------------------------------------
#autoryzacja + autentykacja + wybów do update i delete