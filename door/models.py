from django.db import models
from owner.models import Owner
from django.utils.translation import gettext_lazy as _

class FireDoor(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name=_("Door Code"))
    location = models.CharField(max_length=100, verbose_name=_("Location"))
    installation_date = models.DateField(verbose_name=_("Installation Date"))
    next_maintenance_date = models.DateField(verbose_name=_("Next Maintenance Date"))
    active = models.BooleanField(default=True, verbose_name=_("Active/Inactive"))
    
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name=_("Owner"))

    def __str__(self):
        return f"{self.code} - {self.location}"

    class Meta:
        verbose_name = _("Fire Door")
        verbose_name_plural = _("Fire Doors")
