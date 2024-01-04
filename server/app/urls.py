from . import views
from django.urls import path

urlpatterns = [
    path('home',views.home , name = 'home'),
    path('update/<int:pk>',views.detailsupdate , name = 'update'),

    path('aws',views.getKey , name="getKey"),

    # Big H
    path('table',views.TableApi.as_view()),
    path('table/<int:pk>',views.TableApi.as_view()),

    path('role',views.RoleApi.as_view()),
    path('role/<int:pk>',views.RoleApi.as_view()),

    # Big U 
    path('persona',views.PersonaApi.as_view()),

    # rawsql
    path('employee-details',views.employeedetails , name = "employee-details")
]
