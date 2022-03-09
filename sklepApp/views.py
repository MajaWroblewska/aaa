from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, FormView, UpdateView, DeleteView

# Create your views here.
from sklepApp.models import Produkt
from sklepApp.forms import ProduktForm


#--------------------------------------------------------------------------
class ProduktView(View):
    def get(self,request):
        return render(request,
                      template_name='produkt.html',
                      context={'produkty': Produkt.objects.all()}
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

class ProduktDeleteView(DeleteView):
    template_name = 'produkt_delete_form.html'
    model = Produkt
    success_url = reverse_lazy('produkt')
#--------------------------------------------------------------------------
#autoryzacja + autentykacja + wybów do update i delete