# Create your views here.
# CreateView => adaugare date in form
# UpdateView => modificare date in form
# DeleteView => stergere in DB
# IndexView => informare cu privire la formular
# ListView => informatii de tip lista din DB
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from aplicatie1.models import Location


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    # fields = '__all__'
    fields = ['city', 'country']
    template_name = "aplicatie1/location_form.html"

    def get_success_url(self):
        return reverse('aplicatie1:listare')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    # fields = '__all__'
    fields = ['city', 'country']
    template_name = "aplicatie1/location_form.html"

    def get_success_url(self):
        return reverse('aplicatie1:listare')


class ListLocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'
