from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Vacancy
from django.urls import reverse_lazy
from .forms import VacancyForm

# Create your views here.

def home(request):
  return HttpResponse("Hello, Django!")

class VacancyListView(ListView):
  model = Vacancy
  template_name = "core/vacancy_list.html"
  context_object_name = "vacancies"

class VacancyDetailView(DetailView):
  model = Vacancy
  template_name = "core/vacancy_detail.html"
  context_object_name = "vacancy"

class VacancyCreateView(CreateView):
  model = Vacancy
  form_class = VacancyForm
  template_name = "core/vacancy_form.html"
  success_url = reverse_lazy("vacancy_list")