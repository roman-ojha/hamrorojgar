from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def view_job_application(request, id):
    print(id)
    pass
