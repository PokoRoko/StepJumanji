from django.contrib import admin

from step_job.models import Application, Company, Resume, Specialty, Vacancy


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("title", "salary_min", "salary_max", "specialty", "published_at")
    fields = (
        "company",
        "title",
        "specialty",
        "skills",
        "description",
        "salary_min",
        "salary_max",
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass

