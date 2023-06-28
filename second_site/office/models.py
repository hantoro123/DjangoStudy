from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    heartrate = models.IntegerField(default=60) # null=True로 널값으로 초기값 설정 가능

    def __str__(self):

        return f"{self.last_name},{self.first_name} is {self.age} years old."