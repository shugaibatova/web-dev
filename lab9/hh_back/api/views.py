from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CompanySerializers, VacancySerializers
from .models import Company, Vacancy

# Create your views here.
# Write API endpoints with JSON format:
# /api/companies - List of all Companies
# /api/companies/<int:id>/ - Get one Company
# /api/companies/<int:id>/vacancies/ - List of Vacancies by Company
# /api/vacancies/ - List of all Vacancies
# /api/vacancies/<int:id>/ - Get one Vacancy
# /api/vacancies/top_ten/ - List of top 10 vacancies sorted by decreasing salary
#
def get_top_ten():
    return Vacancy.objects.order_by('-salary')[:10]
@api_view(['GET'])
def companies_list(request):
    companies=Company.objects.all()
    serializer=CompanySerializers(companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def  one_company(request, id):
    company=Company.objects.get(id=id)
    serializer=CompanySerializers(company)
    return Response(serializer.data)
@api_view(['GET'])
def list_vacancies_by_company(request, id):
    vacancy=Vacancy.objects.filter(company_id=id)
    serializer=VacancySerializers(vacancy, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def vacancies_list(request):
    vacancies=Vacancy.objects.all()
    serializer=VacancySerializers(vacancies, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def  one_vacancy(request, id):
    vacancy=Vacancy.objects.get(id=id)
    serializer=VacancySerializers(vacancy)
    return Response(serializer.data)
@api_view(['GET'])
def top_ten(request):
    vacancy=get_top_ten()
    serializer=VacancySerializers(vacancy, many=True)
    return Response(serializer.data)