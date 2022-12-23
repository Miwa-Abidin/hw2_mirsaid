
from django.contrib import admin
from django.urls import path
from employes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/position/', views.create_position),
    path('api/employee/', views.create_employee),
]
