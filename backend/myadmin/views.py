from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from api.models import JobApplication


@require_http_methods(["GET"])
def view_job_application(request, id):
    job_application = JobApplication.objects.get(id=id)
    return render(request, 'myadmin/view_job_application.html', {'job_application': job_application})
