from django.shortcuts import get_object_or_404
from django.shortcuts import render

from HackathonSamara.apps.main.company import Company


def company_profile(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    services = company.services.all()  # Все услуги компании
    return render(request, 'companies/profile.html', {'company': company, 'services': services})
