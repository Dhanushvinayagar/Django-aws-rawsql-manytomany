from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=20,default="")
    age = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add = True)

# Big H
class TableDb(models.Model):
    table = models.CharField(max_length=30)

    def __str__(self):
        return self.table
    
class UserRole(models.Model):
    
    role = models.CharField(max_length=100)
    publications = models.ManyToManyField(TableDb)

    def __str__(self):
        return self.role


#Big U
class Kpi(models.Model):
    kpi_name = models.CharField(max_length=50)
    kpi_code = models.CharField(max_length=50)
    kpi_section = models.CharField(max_length=30)

    def __str__(self):
        return self.kpi_name

class Filter(models.Model):
    filter_name = models.CharField(max_length=50)
    filter_code = models.CharField(max_length=50)
    filter_column = models.CharField(max_length=50)

    def __str__(self):
        return self.filter_name

class Report(models.Model):
    report_name = models.CharField(max_length=50)
    link = models.TextField()
    category = models.CharField(max_length=50)

    filter = models.ManyToManyField(Filter)
    def __str__(self):
        return self.report_name

class PersonaDb(models.Model):
    persona_name = models.CharField(max_length=50)
    persona_code = models.CharField(max_length=50)
    persona_description = models.TextField()

    kpis = models.ManyToManyField(Kpi)
    filters = models.ManyToManyField(Filter)

    def __str__(self):
        return self.persona_name