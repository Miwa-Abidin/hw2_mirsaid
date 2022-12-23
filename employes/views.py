from django.shortcuts import render

import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Position, Employee
from rest_framework import viewsets
from . serializers import PositionSerializer, EmployeeSerializer
from django.http import JsonResponse

@csrf_exempt
def create_position(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_position = Position.objects.create(**data)
        json_data = {
            "position": new_position.position,
            "department": new_position.department
        }
        return JsonResponse(json_data, safe=False)

    if request.method == "GET":
        positions = Position.objects.all()
        data = []
        for position in positions:
            data.append(
                {
                    "position": position.position,
                    "department": position.department
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_employee(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_employee = Employee.objects.create(**data)
        json_data = {
            "fullname": new_employee.fullname,
            "date_birth": new_employee.date_birth,
            "department": new_employee.department.id,
            "zarik": new_employee.zarik
        }
        return JsonResponse(json_data, safe=False)

    if request.method == "GET":
        employees = Employee.objects.all()
        data = []
        for employee in employees:
            data.append(
                {
                    "fullname": employee.fullname,
                    "date_birth": employee.date_birth,
                    "department": employee.department.id,
                    "zarik": employee.zarik
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


class PositionCreateListView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer



class EmployeeCreateListView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



