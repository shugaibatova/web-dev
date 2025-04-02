from django.urls import path
from .views import *
# Create your views here.
# Write API endpoints with JSON format:
# /api/companies - List of all Companies
# /api/companies/<int:id>/ - Get one Company
# /api/companies/<int:id>/vacancies/ - List of Vacancies by Company
# /api/vacancies/ - List of all Vacancies
# /api/vacancies/<int:id>/ - Get one Vacancy
# /api/vacancies/top_ten/ - List of top 10 vacancies sorted by decreasing salary
#
urlpatterns=[
    path('companies/', companies_list),
    path('companies/<int:id>/', one_company),
    path('companies/<int:id>/vacancies/', list_vacancies_by_company),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:id>/', one_vacancy),
    path('vacancies/top_ten/', top_ten),
]