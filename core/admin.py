from django.contrib import admin
from .models import Vacancy

# Register your models here.
@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
  list_display = ("title", "company", "salary_from", "is_remote")
  list_filter = ("is_remote",)
  search_fields = ("title", "company")