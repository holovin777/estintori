from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class OwnerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'owner'
    verbose_name = _("Owner")

