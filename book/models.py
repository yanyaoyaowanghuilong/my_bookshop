from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=200)

class PeopleInfo(models.Model):
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=100)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
