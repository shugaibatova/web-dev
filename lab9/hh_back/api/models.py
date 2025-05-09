from django.db import models
# Company
# name - CharField
# description - TextField
# city - CharField
# address - TextField
# Vacancy
# name - CharField
# description - TextField
# salary - FloatField
# company - ForeignKey
class Company(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    city=models.CharField(max_length=100)
    address=models.TextField()
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    salary=models.FloatField()
    company=models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")

    def __str__(self):
        return self.name

# Create your models here.
