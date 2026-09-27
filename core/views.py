from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Vacancy

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