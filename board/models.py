from datetime import datetime

from django.db import models

# Create your models here.
class News(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.TextField()
    regdate=models.CharField(max_length=20)
    view=models.IntegerField(default=0)
    content=models.TextField()
    category=models.CharField(max_length=20)

    class Meta:
        db_table = 'news'
        ordering = ['-id']