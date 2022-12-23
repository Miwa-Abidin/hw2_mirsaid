from rest_framework import serializers

from . models import Position, Employee

class PositionSerializer(serializers.Serializer):
    position = serializers.CharField(max_length=30)
    department = serializers.CharField(max_length=30)

    def create(self, validated_data):
        position = Position.objects.create(**validated_data)
        department = Position.objects.create(**validated_data)

        return position, department

    def update(self, instance, validated_data):
        instance.position = validated_data['position']
        instance.department = validated_data['department']

        return instance


class EmployeeSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=30)
    date_birth = serializers.CharField(max_length=20)
    zarik = serializers.CharField()

    def create(self, validated_data):
        fullname = Employee.objects.create(**validated_data)
        zarik = Employee.objects.create(**validated_data)

        return fullname, zarik

    def update(self, instance, validated_data):
        instance.fullname = validated_data['fullname']
        instance.date_birth = validated_data['date_birth']
        instance.department = validated_data['department']
        instance.zarik = validated_data['zarik']

        return instance
