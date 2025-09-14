# svodex_web/views.py

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from reference.models import Reference, Service, Certificate, Stat


def home(request):
    references = Reference.objects.all()[:3]
    services = Service.objects.all()[:3]
    stats = Stat.objects.all()
    references_home = Reference.objects.all().order_by('-date_added')[:3]
    context = {
        'references': references,
        'services': services,
        'stats': stats,
        'references_home': references_home,
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def certificate_list(request):
    certificates = Certificate.objects.all()
    context = {'certificates': certificates}
    return render(request, 'reference/certificate_list.html', context)


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