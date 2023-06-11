from django.db import models
from api.models import government, district, municipality
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

        def get_label(self, job_type) -> str:
            if job_type == self.PARTTIME.value:
                return self.PARTTIME.label
            elif job_type == self.FULLTIME.value:
                return self.FULLTIME.label
            elif job_type == self.CONTRACT.value:
                return self.CONTRACT.label
            elif job_type == self.TEMPORARY:
                return self.TEMPORARY.label
            elif job_type == self.INTERNSHIP:
                return self.INTERNSHIP.label
            else:
                return ""

    opened_at = models.DateField(default=timezone.now)
    job_type = models.CharField(max_length=15, choices=JobTypeChoices.choices)
    government = models.ForeignKey(
        government.Government, on_delete=models.CASCADE, related_name='opened_by')
    job_location_desc = models.CharField(max_length=100)
    # position

    def __str__(self) -> str:
        return f"{self.pk}"

    def is_closed(self):  # for algolia 'should_index' field
        return self.is_opened

    def get_tag_list(self):  # for algolia 'tags'
        return [f"{self.government.location.district} {self.government.location.municipality}"]

    def get_job_type(self):
        return Vacancy.JobTypeChoices(self.job_type).get_label(job_type=self.job_type)
