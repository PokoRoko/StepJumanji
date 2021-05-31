from django.db import models


class Company(models.Model):
    name = models.CharField
    location = models.CharField
    logo = models.URLField
    description = models.CharField
    employee_count = models.IntegerField


class Specialty(models.Model):
    code = models.CharField
    title = models.CharField
    picture = models.URLField


class Vacancy(models.Model):
    title = models.CharField
    specialty = models.ManyToManyField(Specialty, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField
    description = models.CharField
    salary_min = models.IntegerField
    salary_max = models.IntegerField
    published_at = models.DateTimeField
