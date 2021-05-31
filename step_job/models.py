from django.core.exceptions import ValidationError
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.URLField
    description = models.CharField
    employee_count = models.IntegerField


class Specialty(models.Model):
    code = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=64)
    picture = models.URLField


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField
    description = models.CharField
    salary_min = models.IntegerField
    salary_max = models.IntegerField
    published_at = models.DateTimeField

    # Подглядел с вебинара, но уж очень хотелось использовать
    def clean(self):
        if self.salary_max > self.salary_min:
            raise ValidationError()
