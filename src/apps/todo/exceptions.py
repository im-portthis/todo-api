from django.utils.translation import ugettext_lazy as _


class Error(Exception):
    message = 'bad request'


class TaskAlreadyAssigned(Error):
    message = _('Задача уже назначена')


class AccountTaskDoesNotExist(Error):
    message = _('Задача не назначена на указанного пользователя или не существует')
