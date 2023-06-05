from django.db import models
from django.utils.translation import gettext_lazy as _


class Citizen(models.Model):
    f_name = models.CharField(_("First name"), max_length=30)
    m_name = models.CharField(_("Middle name"), max_length=30, null=True)
    l_name = models.CharField(_("Last name"), max_length=30)
    mobile = models.IntegerField()
    date_of_birth = models.DateField()

    class GenderChoice(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHERS = 'O', 'Others'
    gender = models.CharField(
        max_length=3, choices=GenderChoice.choices)
    citizenship_no = models.CharField(max_length=200)

    def name(self):
        if self.m_name:
            return f"{self.f_name} {self.m_name} {self.l_name}"
        else:
            return f"{self.f_name} {self.l_name}"
