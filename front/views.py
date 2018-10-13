from django.shortcuts import render
from django.http import HttpResponse
from front.models import Score,Student,Course,Teacher
from django.db.models import Avg
from django.db import connection


def index(requrest):
    # 1.查询平均成绩大于60分的同学的id和平均成绩
    students = Student.objects.annotate(score_avg=Avg("score__number")).filter(score_avg__gt=60).values('id','score_avg')
    for stu in students:
        print(stu)
    print(connection.queries)
    return HttpResponse("success")
