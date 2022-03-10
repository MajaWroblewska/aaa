from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, FormView, UpdateView, DeleteView

# Create your views here.
from sklepApp.models import Produkt
from sklepApp.forms import ProduktForm, ProduktSelectUpdateForm


#--------------------------------------------------------------------------
class ProduktView(View):
    def get(self,request):
        return render(request,
                      template_name='produkt.html',
                      context={'produkty': Produkt.objects.all()},
                      )

class ProduktCreateView(FormView):
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

class ProduktUpdateView(UpdateView):
    template_name = 'produkt_form.html'
    model = Produkt
    form_class = ProduktForm
    success_url = reverse_lazy('produkt')


class ProduktSelectUpdateView(FormView):
    template_name = 'produkt_select_form.html'
    form_class = ProduktSelectUpdateForm
    success_url = reverse_lazy('produkt')

    def form_valid(self, form):
        result = super().form_valid(form)

        moje_produkty = form.cleaned_data

        # print(moje_produkty)
        # print(moje_produkty['produkt1'])  #'produkt1 to pole z forms.py w class ProduktSelectUpdateForm
        # print(dir(moje_produkty['produkt1']))
        # print(moje_produkty['produkt1'].id)

        id_produkt = moje_produkty['produkt1'].id
        # print(id_produkt)

        response = redirect('produkt_update', pk=id_produkt)

        # return result
        return response




#-#-##-#-#-#-#--#-#-#-##-#--##--#-##--#-#-#
class ProduktDeleteView(DeleteView):
    template_name = 'produkt_delete_form.html'
    model = Produkt
    success_url = reverse_lazy('produkt')
#--------------------------------------------------------------------------
#autoryzacja + autentykacja + wybów do update i delete