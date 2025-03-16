from django.db import models
from owner.models import Owner

class FireExtinguisher(models.Model):

    TYPES = [
        ('CO2', 'Carbon Dioxide (CO2)'),
        ('POWDER', 'ABC Powder'),
        ('FOAM', 'AFFF Foam'),
    ]

    code = models.CharField(max_length=20, unique=True, verbose_name="Extinguisher Code")
    type = models.CharField(max_length=20, choices=TYPES, verbose_name="Extinguisher Type")
    net_weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Net Weight (kg)")
    manufacture_date = models.DateField(verbose_name="Manufacture Date")
    revision_expiry_date = models.DateField(verbose_name="Revision Expiry Date")
    test_expiry_date = models.DateField(verbose_name="Test Expiry Date")
    next_maintenance_date = models.DateField(verbose_name="Next Maintenance Date")
    location = models.CharField(max_length=100, verbose_name="Location")
    active = models.BooleanField(default=True, verbose_name="Active/Inactive")

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name="Owner")

    def __str__(self):
        return f"{self.code} - ({self.type})"
