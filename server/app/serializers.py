from .models import *
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        # exclude = ['date']

#Big H
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableDb
        fields = '__all__'
        # exclude = ['date']

class RoleSerializer(serializers.ModelSerializer):
    publications = TableSerializer(many=True)
    class Meta:
        model = UserRole
        fields = '__all__'
        # exclude = ['date']

# Big U
class KpiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kpi
        fields = '__all__'
        # exclude = ['date']

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    filters = FilterSerializer(many=True)
    class Meta:
        model = Report
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    kpis = KpiSerializer(many=True)
    filters = FilterSerializer(many=True)
    class Meta:
        model = PersonaDb
        fields = '__all__'
        # exclude = ['date']
