from django.db import models

# Create your models here.
# 스키마 정의
# 데이터베이스 테이블을 정의하고,
# 각각의 컬럼(필드) 정의
class Article(models.Model):
    # id : integer 자동으로 정의(Primary Key)  
    # id = models.AutoField(primary_key=True) -> Integer 값이 자동으로 하나씩 증가(AUTOINCREMENT)
    # CharField - 필수인자로 max_length 지정
    title = models.CharField(max_length=10)
    context = models.TextField()
    # DateTimeField
    #       auto_now_add : 생성시 자동으로 입력
    #       auto_now : 수정시마다 자동으로 저장
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id} : {self.title}'

# models.py : python 클래스 정의
#           : 모델 설계도
# makemigrations : migration 파일 생성
#           : DB 설계도 작성
# migrate : migration 파일 DB 반영
