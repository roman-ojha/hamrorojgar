from django.db import models
from . import Government
from django.utils import timezone


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_opened = models.BooleanField(default=True)
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()

    class JobTypeChoices(models.TextChoices):
        PARTTIME = "PART", 'Part-Time',
        FULLTIME = "FULL", 'Full-Time',
        CONTRACT = "CONTRACT", 'Contract',
        TEMPORARY = "TEMPO", 'Temporary',
        INTERNSHIP = "INTERN", 'Internship',
    opened_on = models.DateField(default=timezone.now)
    job_type = models.CharField(max_length=15, choices=JobTypeChoices.choices)
    government = models.ForeignKey(
        Government, on_delete=models.CASCADE, related_name='opened_by')
    # job_location_desc
    # position

    def __str__(self) -> str:
        return f"{self.pk}"
