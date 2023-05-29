from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from api.models import JobApplication
from django.http import HttpResponseRedirect
from django.http import HttpRequest


@require_http_methods(["GET"])
def view_job_application(request, id):
    try:
        job_application = JobApplication.objects.get(id=id)
        return render(request, 'myadmin/view_job_application.html', {'job_application': job_application})
    except JobApplication.DoesNotExist:
        return render(request, 'myadmin/view_job_application.html', {'error': 'Provided job application id does not exist'})


@require_http_methods(["POST"])
def approve_job_application(request: HttpRequest, id):
    job_application = JobApplication.objects.get(id=id)
    job_application.is_approved = True
    job_application.save()
    return HttpResponseRedirect(f"/admin/api/jobapplication/?vacancy_id={job_application.vacancy}")


@require_http_methods(["POST"])
def disapprove_job_application(request, id):
    job_application = JobApplication.objects.get(id=id)
    job_application.is_approved = False
    job_application.save()
    return HttpResponseRedirect(f"/admin/api/jobapplication/?vacancy_id={job_application.vacancy}")
