from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vacancies/", views.VacancyListView.as_view(), name="vacancy_list"),
]
