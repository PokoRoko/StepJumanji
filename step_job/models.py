from django.contrib.auth.models import User
from django.db import models

from StepikJumanji.settings import (MEDIA_COMPANY_IMAGE_DIR,
                                    MEDIA_SPECIALITY_IMAGE_DIR)


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField(default='https://place-hold.it/100x60', upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.TextField(max_length=2056)
    employee_count = models.PositiveIntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="companies", null=True)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name.title()


class Specialty(models.Model):
    code = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=64)
    picture = models.ImageField(default='https://place-hold.it/100x60', upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"

    def __str__(self):
        return self.title.title()


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=64)
    description = models.TextField(max_length=2056)
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title.title()


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=12)
    written_cover_letter = models.TextField(max_length=2058)
    vacancy = models.ForeignKey(Vacancy, related_name="applications", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="applications", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"

    def __str__(self):
        return f"Application {self.user} to {self.vacancy}"


class Resume(models.Model):
    class Education(models.TextChoices):
        missing = 'Отсутствует'
        secondary = 'Среднее'
        vocational = 'Средне-специальное'
        incomplete_higher = 'Неполное высшее'
        higher = 'Высшее'

    class Grade(models.TextChoices):
        intern = 'intern'
        junior = 'junior'
        middle = 'middle'
        senior = 'senior'
        lead = 'lead'

    class Specialty(models.TextChoices):
        frontend = 'Фронтенд'
        backend = 'Бэкенд'
        gamedev = 'Геймдев'
        devops = 'Девопс'
        design = 'Дизайн'
        products = 'Продукты'
        management = 'Менеджмент'
        testing = 'Тестирование'

    class WorkStatus(models.TextChoices):
        not_in_search = 'Не ищу работу'
        consideration = 'Рассматриваю предложения'
        in_search = 'Ищу работу'

    user = models.OneToOneField(User, related_name="Resumes", on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    status = models.CharField(choices=WorkStatus.choices, max_length=64)
    salary = models.PositiveIntegerField()
    specialty = models.CharField(choices=Specialty.choices, max_length=512)
    grade = models.CharField(choices=Grade.choices, max_length=64)
    education = models.CharField(choices=Education.choices, max_length=64)
    experience = models.CharField(max_length=512)
    portfolio = models.TextField(max_length=1028)

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

    def __str__(self):
        return f"Resume {self.user}"
