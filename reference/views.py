# reference/views.py

from django.shortcuts import render, get_object_or_404
from .models import Reference, Service, Certificate, Stat

def reference_list(request):
    references = Reference.objects.all()
    context = {'references': references}
    return render(request, 'reference/reference_list.html', context)

def reference_detail(request, pk):
    reference = get_object_or_404(Reference, pk=pk)
    context = {'reference': reference}
    return render(request, 'reference/reference_detail.html', context)

def service_list(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'reference/service_list.html', context)

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    context = {
        'service': service
    }
    return render(request, 'reference/service_detail.html', context)