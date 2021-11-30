from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class DB(models.Model):
    규모 = models.CharField(max_length=50)
    병원 = models.CharField(max_length=50)
    보철물 = models.CharField(max_length=50)
    최저가 = models.CharField(max_length=50)
    최고가 = models.CharField(max_length=50)
    소재지 = models.CharField(max_length=50)
    지역 = models.CharField(max_length=50)
    구 = models.CharField(max_length=50)

    def __str__(self):
        return self.병원
