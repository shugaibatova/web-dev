# from django.urls import path
# from .views import *
# # Create your views here.
# # Write API endpoints with JSON format:
# # /api/companies - List of all Companies
# # /api/companies/<int:id>/ - Get one Company
# # /api/companies/<int:id>/vacancies/ - List of Vacancies by Company
# # /api/vacancies/ - List of all Vacancies
# # /api/vacancies/<int:id>/ - Get one Vacancy
# # /api/vacancies/top_ten/ - List of top 10 vacancies sorted by decreasing salary
# #
# urlpatterns=[
#     path('companies/', companies_list),
#     path('companies/<int:id>/', one_company),
#     path('companies/<int:id>/vacancies/', list_vacancies_by_company),
#     path('vacancies/', vacancies_list),
#     path('vacancies/<int:id>/', one_vacancy),
#     path('vacancies/top_ten/', top_ten),

# ]
from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list),
    path('companies/<int:id>/', views.company_detail),
    path('companies/<int:id>/vacancies/', views.company_vacancies),
    path('vacancies/', views.VacancyList.as_view()),
    path('vacancies/<int:id>/', views.VacancyDetail.as_view()),
    path('vacancies/top_ten/', views.top_ten_vacancies),
]
