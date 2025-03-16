from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100, verbose_name="Owner Name")
    address = models.CharField(max_length=255, blank=True, verbose_name="Address")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Phone Number")
    email = models.EmailField(blank=True, verbose_name="Email")
    is_company = models.BooleanField(default=False, verbose_name="Is a Company?")

    def __str__(self):
        return self.name
