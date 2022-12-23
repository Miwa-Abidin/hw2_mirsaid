
from django.db import models


class Position(models.Model):
    position = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.position} - {self.department}'

class Employee(models.Model):
    fullname = models.CharField(max_length=30, verbose_name='ФИО')
    date_birth = models.CharField(max_length=20, verbose_name='Год рождения')
    department = models.ForeignKey(Position, related_name='departments', on_delete=models.CASCADE)
    zarik = models.IntegerField()


    def __str__(self):
        return f'{self.fullname} - {self.zarik}'



