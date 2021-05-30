from django.http import (Http404, HttpResponseBadRequest,
                         HttpResponseForbidden, HttpResponseNotFound,
                         HttpResponseServerError)
from django.shortcuts import render


def custom_handler400(request, exception):
    return HttpResponseBadRequest(f'Неверный запрос!\n{exception}')


def custom_handler403(request, exception):
    return HttpResponseForbidden(f'Доступ запрещен!\n{exception}')


def custom_handler404(request, exception):
    return HttpResponseNotFound(f'Ресурс не найден!\n{exception}')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')