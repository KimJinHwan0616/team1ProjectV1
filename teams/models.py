from django.db import models

# Create your models here.

class Stadiums(models.Model):
    id = models.AutoField(primary_key = True)
    stname = models.CharField(max_length=256)
    opdate = models.CharField(max_length=256)
    hteam = models.CharField(max_length=256)
    accnum = models.IntegerField()
    location = models.CharField(max_length=256)
    addrstmp = models.IntegerField()
    addrkey = models.CharField(max_length=256)

    class Meta:
        db_table = 'stadiums'

