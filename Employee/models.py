from django.db import models


# Create your models here.

class Employee_s(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    is_married = models.BooleanField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Employee_s'
        ordering = ['-id']
