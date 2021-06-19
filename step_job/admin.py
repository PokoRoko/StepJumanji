from django.contrib import admin

from step_job.models import Application, Company, Resume, Specialty, Vacancy


class VacancyInline(admin.TabularInline):
    model = Vacancy
    extra = 0


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ("name", "id")

    list_filter = ("location",)

    list_display = (
        "name",
        "owner",
        "location",
        "employee_count",
    )
    readonly_fields = ("owner",)
    fields = (
        "name",
        "owner",
        "location",
        "description",
        "employee_count",
        "logo",
    )

    inlines = [VacancyInline]
    save_as = True


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):

    search_fields = ("title", "description")

    list_filter = ("specialty",)

    list_display = ("title", "salary_min", "salary_max", "specialty", "published_at")

    readonly_fields = ("specialty", "company")

    fields = (
        "company",
        "title",
        "specialty",
        "skills",
        "description",
        "salary_min",
        "salary_max",
    )
    save_as = True


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_filter = ("specialty",)

    list_display = ("user", "name", "surname", "status", "salary", "specialty", "grade")

    radio_fields = {"status": admin.VERTICAL}

    readonly_fields = ("status", "specialty", "grade")

    fields = (
        "user",
        "name",
        "surname",
        "status",
        "salary",
        "specialty",
        "grade",
        "education",
        "experience",
        "portfolio",
    )
