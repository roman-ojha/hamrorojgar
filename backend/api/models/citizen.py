from django.db import models


# class Citizen(models.Model):
#     f_name = models.CharField(max_length=30)
#     m_name = models.CharField(max_length=30, null=True)
#     l_name = models.CharField(max_length=30)
#     mobile = models.IntegerField()
#     date_of_birth = models.DateField()

#     class GenderChoice(models.TextChoices):
#         MALE = 'M', 'Male'
#         FEMALE = 'F', 'Female'
#         OTHERS = 'O', 'Others'
#     gender = models.CharField(
#         max_length=3, choices=GenderChoice.choices)
#     nationality = models.CharField(max_length=80)
#     citizenship_no = models.CharField(max_length=200)
#     # Use url shortener package
#     photo = models.CharField(max_length=100, null=True)
#     # permanent_address
#     # temporary_address
