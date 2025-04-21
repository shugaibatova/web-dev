from rest_framework import serializers
from .models import Company, Vacancy

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'

class VacancySerializers(serializers.ModelSerializer):
    class Meta:
        model= Vacancy
        fields='__all__'
