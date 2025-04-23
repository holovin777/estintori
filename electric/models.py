from django.db import models
from django.utils.translation import gettext_lazy as _
from owner.models import Owner

class ElectricPanel(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name=_("Panel Code"))
    installation_date = models.DateField(verbose_name=_("Installation Date"))
    last_maintenance_date = models.DateField(verbose_name=_("Last Maintenance"))
    next_maintenance_date = models.DateField(verbose_name=_("Next Maintenance"))
    location = models.CharField(max_length=100, verbose_name=_("Location"))
    active = models.BooleanField(default=True, verbose_name=_("Active/Inactive"))

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name=_("Owner"))

    def __str__(self):
        return f"{self.code} - {self.location}"

    class Meta:
        verbose_name = _("Electric Panel")
        verbose_name_plural = _("Electric Panels")
