from django.utils.translation import gettext_lazy as _
from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Owner Name"))
    address = models.CharField(max_length=255, blank=True, verbose_name=_("Address"))
    phone = models.CharField(max_length=20, blank=True, verbose_name=_("Phone Number"))
    email = models.EmailField(blank=True, verbose_name=_("Email"))
    is_company = models.BooleanField(default=False, verbose_name=_("Is a Company?"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Owner")
        verbose_name_plural = _("Owners")
