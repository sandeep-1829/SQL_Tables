from django.db import models

# Create your models here.


class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    
    def __str__(self):
        return self.dname

class Emp(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100,primary_key=True)
    deptno=models.OneToOneField(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename

class Bonus(models.Model):
    ename=models.OneToOneField(Emp,on_delete=models.CASCADE)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()

    def __str__(self):
        return self.job


class Salgrade(models.Model):
    grade=models.CharField(max_length=100)
    losal=models.PositiveIntegerField()
    hisal=models.PositiveIntegerField()

    def __str__(self):
        return self.grade
    


