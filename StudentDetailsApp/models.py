from django.db import models

# Create your models here.
class StudentData(models.Model):
    roll=models.IntegerField()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    student_class=models.CharField(max_length=100)
    student_section=models.CharField(max_length=5)
    telgu_mark=models.IntegerField()
    hindi_mark=models.IntegerField()
    english_mark=models.IntegerField()
    math_mark=models.IntegerField()
    science_mark=models.IntegerField()
    social_mark=models.IntegerField()