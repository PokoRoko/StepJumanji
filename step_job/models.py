from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from StepikJumanji.settings import (MEDIA_COMPANY_IMAGE_DIR,
                                    MEDIA_SPECIALITY_IMAGE_DIR)


class Company(models.Model):
    name = models.CharField(_("Название"), max_length=64)
    location = models.CharField(_("Месторасположение"), max_length=64)
    logo = models.ImageField(_("Логотип"), default='https://place-hold.it/100x60', upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.TextField(_("Описание"), max_length=2056)
    employee_count = models.PositiveIntegerField(_("Количество сотрудников"))
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="companies",
                                 verbose_name=_("Владелец"), null=True)

    class Meta:
        verbose_name = _("Компания")
        verbose_name_plural = _("Компании")

    def __str__(self):
        return self.name.title()


class Specialty(models.Model):
    code = models.CharField(_("Код"), max_length=64, unique=True)
    title = models.CharField(_("Описание"), max_length=64)
    picture = models.ImageField(_("Картинка"), default='https://place-hold.it/100x60', upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

    class Meta:
        verbose_name = _("Специализация")
        verbose_name_plural = _("Специализации")

    def __str__(self):
        return self.title.title()


class Vacancy(models.Model):
    title = models.CharField(_("Название вакансии"), max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE,
                                  related_name="vacancies", verbose_name=_("Специальность"))
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name="vacancies", verbose_name=_("Компания"))
    skills = models.CharField(_("Навыки"), max_length=512)
    description = models.TextField(_("Описание"), max_length=2056)
    salary_min = models.PositiveIntegerField(_("Зарплато от"),)
    salary_max = models.PositiveIntegerField(_("Зарплата до"),)
    published_at = models.DateTimeField(_("Дата публикации"), auto_now_add=True, blank=True)

    class Meta:
        verbose_name = _("Вакансия")
        verbose_name_plural = _("Вакансии")

    def __str__(self):
        return self.title.title()


class Application(models.Model):
    written_username = models.CharField(_("Ваше имя"), max_length=64)
    written_phone = models.CharField(_("Ваш телефон"), max_length=16)
    written_cover_letter = models.TextField(_("Сопроводительное письмо"), max_length=2058)
    vacancy = models.ForeignKey(Vacancy, related_name="applications",
                                on_delete=models.CASCADE, verbose_name=_("Вакансия"))
    user = models.ForeignKey(User, related_name="applications",
                             on_delete=models.CASCADE, verbose_name=_("Пользователь"))

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

    class WorkStatus(models.TextChoices):
        not_in_search = _('Не ищу работу')
        consideration = _('Рассматриваю предложения')
        in_search = _('Ищу работу')

    user = models.OneToOneField(User, related_name="resumes", on_delete=models.CASCADE, verbose_name=_("Пользователь"),)
    name = models.CharField(_("Имя"), max_length=64)
    surname = models.CharField(_("Фамилия"), max_length=64)
    status = models.CharField(_("Статус"), choices=WorkStatus.choices, max_length=64)
    salary = models.PositiveIntegerField(_("Ожидаемая зарплата"), )
    specialty = models.ForeignKey(Specialty, related_name="resumes",
                                  on_delete=models.CASCADE, verbose_name=_("Специальность"))
    grade = models.CharField(_("Уровень квалификации"), choices=Grade.choices, max_length=64)
    education = models.CharField(_("Образование"), choices=Education.choices, max_length=64)
    experience = models.CharField(_("Опыт работы"), max_length=512)
    portfolio = models.TextField(_("Портфолио"), max_length=1028)

    class Meta:
        verbose_name = _("Резюме")
        verbose_name_plural = _("Резюме")

    def __str__(self):
        return f"Resume {self.user}"
