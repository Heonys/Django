from django.db import models

# Create your models here.


####  makemigration >> 명령어는 models.py에 쓰는 내용을 DB와 연동시킬 파이썬 파일로 만들어주는 역활
####  class 하나가 하나의 DB의 테이블을 만듬

class MyTable(models.Model):
    text = models.CharField(max_length=200)
    
    
class MyTable2(models.Model):
    content = models.TextField()