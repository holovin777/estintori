from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ExtinguisherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'extinguisher'
    verbose_name = _("Extinguisher")
