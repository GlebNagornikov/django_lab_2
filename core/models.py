from django.db import models

# Create your models here.
class Vacancy(models.Model):
  title = models.CharField(max_length=200)
  company = models.CharField(max_length=150)
  salary_from = models.PositiveIntegerField()
  is_remote = models.BooleanField(default=False)

  def __str__(self):
      return self.title