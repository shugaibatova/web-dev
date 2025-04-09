# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .serializers import CompanySerializers, VacancySerializers, Api_newSerializers
# from .models import Company, Vacancy, Api_new

# # Create your views here.
# # Write API endpoints with JSON format:
# # /api/companies - List of all Companies
# # /api/companies/<int:id>/ - Get one Company
# # /api/companies/<int:id>/vacancies/ - List of Vacancies by Company
# # /api/vacancies/ - List of all Vacancies
# # /api/vacancies/<int:id>/ - Get one Vacancy
# # /api/vacancies/top_ten/ - List of top 10 vacancies sorted by decreasing salary
# #
# def get_top_ten():
#     return Vacancy.objects.order_by('-salary')[:10]
# @api_view(['GET', 'POST'])
# def companies_list(request):
#     companies=Company.objects.all()
#     serializer=CompanySerializers(companies, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def  one_company(request, id):
#     company=Company.objects.get(id=id)
#     serializer=CompanySerializers(company)
#     return Response(serializer.data)
# @api_view(['GET'])
# def list_vacancies_by_company(request, id):
#     vacancy=Vacancy.objects.filter(company_id=id)
#     serializer=VacancySerializers(vacancy, many=True)
#     return Response(serializer.data)
# @api_view(['GET'])
# def vacancies_list(request):
#     vacancies=Vacancy.objects.all()
#     serializer=VacancySerializers(vacancies, many=True)
#     return Response(serializer.data)
# @api_view(['GET'])
# def  one_vacancy(request, id):
#     vacancy=Vacancy.objects.get(id=id)
#     serializer=VacancySerializers(vacancy)
#     return Response(serializer.data)
# @api_view(['GET'])
# def top_ten(request):
#     vacancy=get_top_ten()
#     serializer=VacancySerializers(vacancy, many=True)
#     return Response(serializer.data)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

# Function-based views for Company
@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return Response({'error': 'Company not found'}, status=404)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        company.delete()
        return Response(status=204)

@api_view(['GET'])
def company_vacancies(request, id):
    vacancies = Vacancy.objects.filter(company_id=id)
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)

# Class-based views for Vacancy
class VacancyList(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class VacancyDetail(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist:
            return None

    def get(self, request, id):
        vacancy = self.get_object(id)
        if not vacancy:
            return Response({'error': 'Not found'}, status=404)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, id):
        vacancy = self.get_object(id)
        if not vacancy:
            return Response({'error': 'Not found'}, status=404)
        serializer = VacancySerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        vacancy = self.get_object(id)
        if not vacancy:
            return Response({'error': 'Not found'}, status=404)
        vacancy.delete()
        return Response(status=204)

@api_view(['GET'])
def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)
