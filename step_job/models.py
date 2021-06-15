from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
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
        verbose_name = _("Компания")
        verbose_name_plural = _("Компании")

    def __str__(self):
        return self.name.title()


class Specialty(models.Model):
    code = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=64)
    picture = models.ImageField(default='https://place-hold.it/100x60', upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

    class Meta:
        verbose_name = _("Специализация")
        verbose_name_plural = _("Специализации")

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
        verbose_name = _("Вакансия")
        verbose_name_plural = _("Вакансии")

    def __str__(self):
        return self.title.title()


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=12)
    written_cover_letter = models.TextField(max_length=2058)
    vacancy = models.ForeignKey(Vacancy, related_name="applications", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="applications", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Отклик")
        verbose_name_plural = _("Отклики")

    def __str__(self):
        return f"Отзыв {self.user} на '{self.vacancy}'"


class Resume(models.Model):
    class Education(models.TextChoices):
        missing = _('Отсутствует')
        secondary = _('Среднее')
        vocational = _('Средне-специальное')
        incomplete_higher = _('Неполное высшее')
        higher = _('Высшее')

    class Grade(models.TextChoices):
        intern = _('intern')
        junior = _('junior')
        middle = _('middle')
        senior = _('senior')
        lead = _('lead')

    class Specialty(models.TextChoices):
        frontend = _('Фронтенд')
        backend = _('Бэкенд')
        gamedev = _('Геймдев')
        devops = _('Девопс')
        design = _('Дизайн')
        products = _('Продукты')
        management = _('Менеджмент')
        testing = _('Тестирование')

    class WorkStatus(models.TextChoices):
        not_in_search = _('Не ищу работу')
        consideration = _('Рассматриваю предложения')
        in_search = _('Ищу работу')

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
        verbose_name = _("Резюме")
        verbose_name_plural = _("Резюме")

    def __str__(self):
        return f"Resume {self.user}"
