from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ManagerConfig(AppConfig):
    name = 'api.manager'
    verbose_name = _('garage manager')
