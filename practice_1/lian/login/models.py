from django.db import models

# Create your models here.

class user(models.Model):
    username=models.CharField(max_length=30,null=False,primary_key=True)
    pwd=models.CharField(max_length=40,null=False)
    email=models.CharField(max_length=50,null=False)




    def __str__(self):
        return '{},{},{}'.format(self.username,self.pwd,self.email)


class jiaoce(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    carname=models.TextField()
    cardata=models.TextField()
    carurl=models.TextField()
    cartu=models.TextField()
    carjiage=models.TextField()
    def __str__(self):
          return '{},{},{},{},{},{}'.format(self.id,self.carname,self.cardata,self.carurl,self.cartu,self.carjiage)

class mianbaoce(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    carname = models.TextField()
    cardata = models.TextField()
    carurl = models.TextField()
    cartu = models.TextField()
    carjiage = models.TextField()
    def __str__(self):
          return '{},{},{},{},{},{}'.format(self.id,self.carname,self.cardata,self.carurl,self.cartu,self.carjiage)

class mpvce(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    carname = models.TextField()
    cardata = models.TextField()
    carurl = models.TextField()
    cartu = models.TextField()
    carjiage = models.TextField()
    def __str__(self):
          return '{},{},{},{},{},{}'.format(self.id,self.carname,self.cardata,self.carurl,self.cartu,self.carjiage)

class paoce(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    carname = models.TextField()
    cardata = models.TextField()
    carurl = models.TextField()
    cartu = models.TextField()
    carjiage = models.TextField()
    def __str__(self):
          return '{},{},{},{},{},{}'.format(self.id,self.carname,self.cardata,self.carurl,self.cartu,self.carjiage)

class pikace(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    carname = models.TextField()
    cardata = models.TextField()
    carurl = models.TextField()
    cartu = models.TextField()
    carjiage = models.TextField()
    def __str__(self):
          return '{},{},{},{},{},{}'.format(self.id,self.carname,self.cardata,self.carurl,self.cartu,self.carjiage)

class xinnengyuance(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    carname = models.TextField()
    cardata = models.TextField()
    carurl = models.TextField()
    cartu = models.TextField()
    carjiage = models.TextField()
    def __str__(self):
          return '{},{},{},{},{},{}'.format(self.id,self.carname,self.cardata,self.carurl,self.cartu,self.carjiage)

class yueyece(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    carname = models.TextField()
    cardata = models.TextField()
    carurl = models.TextField()
    cartu = models.TextField()
    carjiage = models.TextField()
    def __str__(self):
          return '{},{},{},{},{},{}'.format(self.id,self.carname,self.cardata,self.carurl,self.cartu,self.carjiage)

