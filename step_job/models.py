from django.db import models
from django.contrib.auth.models import User

from StepikJumanji.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField(default='https://place-hold.it/100x60', upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.CharField(max_length=64)
    employee_count = models.PositiveIntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Companies")

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"Company {self.name}"


class Specialty(models.Model):
    code = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=64)
    picture = models.ImageField(default='https://place-hold.it/100x60', upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"

    def __str__(self):
        return f"Specialty {self.title}"


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f"Vacancy {self.title}"


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=12)
    written_cover_letter = models.TextField(max_length=1028)
    vacancy = models.OneToOneField(Vacancy, related_name="applications", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="applications", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"

    def __str__(self):
        return f"Application {self.user} to {self.vacancy}"


class Resume(models.Model):
    class EducationChoices(models.TextChoices):
        missing = 'Отсутствует'
        secondary = 'Среднее'
        vocational = 'Средне-специальное'
        incomplete_higher = 'Неполное высшее'
        higher = 'Высшее'

    class GradeChoices(models.TextChoices):
        intern = 'intern'
        junior = 'junior'
        middle = 'middle'
        senior = 'senior'
        lead = 'lead'

    class SpecialtyChoices(models.TextChoices):
        frontend = 'Фронтенд'
        backend = 'Бэкенд'
        gamedev = 'Геймдев'
        devops = 'Девопс'
        design = 'Дизайн'
        products = 'Продукты'
        management = 'Менеджмент'
        testing = 'Тестирование'

    class WorkStatusChoices(models.TextChoices):
        not_in_search = 'Не ищу работу'
        consideration = 'Рассматриваю предложения'
        in_search = 'Ищу работу'

    user = models.OneToOneField(User, related_name="Resumes", on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    status = models.CharField(choices=WorkStatusChoices, max_length=64)
    salary = models.PositiveIntegerField()
    specialty = models.CharField(choices=SpecialtyChoices, max_length=512)
    grade = models.CharField(choices=GradeChoices, max_length=64)
    education = models.CharField(choices=EducationChoices, max_length=64)
    experience = models.CharField(max_length=512)
    portfolio = models.CharField(max_length=1028)


