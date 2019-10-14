from django.db import models

# Create your models here.
class Md5Status(models.Model):
    id=models.AutoField(primary_key=True,max_length=20)
    md5=models.CharField(max_length=128)
    question_id = models.CharField(max_length=20)
    key = models.CharField()
    source = models.CharField(max_length=10)
    class Meta:
        db_table = 'md5_status'
        managed = 'False'
