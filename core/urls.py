from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vacancies/", views.VacancyListView.as_view(), name="vacancy_list"),
    path("vacancies/<int:pk>/", views.VacancyDetailView.as_view(), name="vacancy_detail"),
]
