from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from api.models.job_application import JobApplication
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.contrib.admin.views.decorators import staff_member_required


@require_http_methods(["GET"])
def index(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/admin/login')
    return render(request, 'pages/dashboard.html')


@require_http_methods(["GET"])
@staff_member_required
def view_job_application(request, id):
    try:
        job_application = JobApplication.objects.get(id=id)
        if job_application.vacancy.government.pk == request.user.pk or request.user.is_superuser:
            return render(request, 'myadmin/view_job_application.html', {'job_application': job_application})
        return HttpResponseRedirect('/admin/api/jobapplication/')
    except JobApplication.DoesNotExist:
        return render(request, 'myadmin/view_job_application.html', {'error': 'Provided job application id does not exist'})


@require_http_methods(["POST"])
@staff_member_required
def approve_job_application(request: HttpRequest, id):
    job_application = JobApplication.objects.get(id=id)
    if job_application.vacancy.government.pk == request.user.pk or request.user.is_superuser:
        job_application.is_approved = True
        job_application.save()
    return HttpResponseRedirect(f"/admin/api/jobapplication/?vacancy_id={job_application.vacancy}")


@require_http_methods(["POST"])
@staff_member_required
def disapprove_job_application(request, id):
    job_application = JobApplication.objects.get(id=id)
    if job_application.vacancy.government.pk == request.user.pk or request.user.is_superuser:
        job_application.is_approved = False
        job_application.save()
    return HttpResponseRedirect(f"/admin/api/jobapplication/?vacancy_id={job_application.vacancy}")
