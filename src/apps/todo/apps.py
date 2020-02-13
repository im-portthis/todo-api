from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TodoConfig(AppConfig):
    name = 'apps.todo'
    verbose_name = _('TODO')
