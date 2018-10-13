from django.shortcuts import render
from django.http import HttpResponse
from front.models import Score, Student, Course, Teacher
from django.db.models import Avg, Count, Sum
from django.db import connection


def index(requrest):
    # 1.查询平均成绩大于60分的同学的id和平均成绩
    students = Student.objects.annotate(score_avg=Avg("score__number")).filter(score_avg__gt=60).values('id',
                                                                                                        'score_avg')
    for stu in students:
        print(stu)
    print(connection.queries)
    return HttpResponse("success")


def index2(requests):
    # 2.查询所有同学的id，姓名，选课的数量，总成绩
    sutdents = Student.objects.annotate(course_num=Count('score'), total=Sum('score__number')).values('id', 'name',
                                                                                                      'course_num',
                                                                                                      'total')
    for student in sutdents:
        print(student)
    print(connection.queries)
    return HttpResponse('success')


def index3(request):
    # 3.查询姓李的老师的个数
    count = Teacher.objects.filter(name__startswith='李').count()
    print(count)
    print(connection.queries)
    return HttpResponse('success')


def index4(request):
    # 3.查询没学过李老师课的同学的id和姓名
    student = Student.objects.exclude(score__course__teacher__name='李老师').values('id', 'name')
    for stu in student:
        print(stu)
    print(connection.queries)
    return HttpResponse('success')


def index5(request):
    # 查询学过课程id为1和2的所有同学的id和姓名

    students = Student.objects.filter(score__course__in=[1, 2]).values('id', 'name').distinct()
    for stu in students:
        print(stu)
    print(connection.queries)
    return HttpResponse('success')


def index6(request):
    # 查询学过黄老师所教的所有科的同学的id和姓名

    return HttpResponse('success')
