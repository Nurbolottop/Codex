from django.shortcuts import render
from apps.base import models
# Create your views here.
def index(request):
    settings = models.Settings.objects.latest("id")
    return render(request, "base/index4.html", locals())