from django.core.exceptions import ValidationError
from django.db import models
import data
from StepikJumanji.settings import BASE_DIR


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.CharField(max_length=64)
    employee_count = models.IntegerField()


class Specialty(models.Model):
    code = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=64)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField(auto_now_add=True, blank=True)


def update_data(moc_data):
    for spec in moc_data.specialties:
        specialty = Specialty(
            code=spec.get("code"),
            title=spec.get("title")
        )
        specialty.save()

    for data_company in moc_data.companies:
        company = Company(
            name=data_company.get("title"),
            location=data_company.get("location"),
            logo=f"{BASE_DIR}/{data_company.get('logo')}",
            description=data_company.get("description"),
            employee_count=data_company.get("employee_count"),
        )
        company.save()

    for job in moc_data.jobs:
        vacancy = Vacancy(
            title=job.get("title"),
            specialty=Specialty.objects.get(code=job.get("specialty")),
            company=Company.objects.get(id=job.get("company")),
            skills=job.get("skills"),
            description=job.get("description"),
            salary_min=job.get("salary_from"),
            salary_max=job.get("salary_to"),
            published_at=job.get("published_at"),
        )
        vacancy.save()
