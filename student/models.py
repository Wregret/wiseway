# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    GENDER=(
        ('M','男'),
        ('F','女'),
    )
    MARRIAGE=(
        ('Y','已婚'),
        ('N','未婚')
    )
    name=models.CharField("姓名", max_length=20)
    gender=models.CharField("性别",max_length=1,choices=GENDER)
    birthday=models.DateField("出生日期")
    marriage=models.CharField('婚姻状况',max_length=1,choices=MARRIAGE)
    birthland=models.CharField('出生地',max_length=30)
    nationality=models.CharField('国籍',max_length=30)
    address=models.CharField('家庭住址',max_length=50)
    postcode=models.CharField('邮政编码',max_length=10)
    email=models.EmailField('电子邮箱')
    phone=models.CharField('电话号码',max_length=20)
    passport=models.CharField('护照号码',max_length=10)
    TARGET=(
        (1,'本科'),
        (2,'硕士'),
        (3,'博士')
    )
    target=models.IntegerField('申请目标',choices=TARGET)
    def __str__(self):
        return self.name.encode('utf8')

class Education(models.Model):
    student=models.ForeignKey('Student')
    fromdate=models.DateField('起始时间')
    todate=models.DateField('结束时间')
    college=models.CharField('系别/学院',max_length=20)
    SCHOOLTYPE=(
        (1,'fulltime'),
        (2,'parttime'),
        (3,'自考'),
        (4,'成人教育')
    )
    schooltype=models.ImageField('学习形式',choices=SCHOOLTYPE)
    major=models.CharField('专业',max_length=20)
    DEGREE=(
        (1,'研究生（硕士）'),
        (2,'本科（学士）'),
        (3,'大专（无学位）')
    )
    degree=models.IntegerField('学历/学位',choices=DEGREE)
    average=models.DecimalField('平均分',max_digits=4,decimal_places=2)
    gpa=models.CharField('GPA',max_length=10)

    def __str__(self):
        return self.name.encode('utf8')


class ResearchExperience(models.Model):
    student=models.ForeignKey('Student')
    date=models.DateField('日期')
    place=models.CharField('研究单位',max_length=20)
    work=models.TextField('研究内容')
    def __str__(self):
        return self.name.encode('utf8')

class Scholarship(models.Model):
    student=models.ForeignKey('Student')
    date=models.DateField('日期')
    title=models.CharField('名称', max_length=10)
    #file=models.FileField('证书',upload_to='/')

    def __str__(self):
        return self.name.encode('utf8')


class Honor(models.Model):
    student=models.ForeignKey('Student')
    date=models.DateField('日期')
    title=models.CharField('名称',max_length=10)
    #file=models.FileField('证书',upload_to='/')

    def __str__(self):
        return self.name.encode('utf8')


class SocialActivity(models.Model):
    student=models.ForeignKey('Student')
    date=models.DateField('日期')
    description=models.TextField('活动/工作')

    def __str__(self):
        return self.name.encode('utf8')


class Internship(models.Model):
    student=models.ForeignKey('Student')
    date=models.DateField('日期')
    place=models.CharField('实习单位',max_length=20)
    department=models.CharField('实习部门',max_length=20)
    work=models.TextField('工作内容')

    def __str__(self):
        return self.name.encode('utf8')


class ComputerSkill(models.Model):
    student=models.ForeignKey('Student')
    software=models.TextField('熟练操作或掌握点软件')

    def __str__(self):
        return self.name.encode('utf8')


class ComputerCertificate(models.Model):
    student=models.ForeignKey('Student')
    name=models.CharField('证书名称', max_length=20)
    date=models.DateField('获得时间')

    def __str__(self):
        return self.name.encode('utf8')


class Hobby(models.Model):
    student=models.ForeignKey('Student')
    hobby=models.CharField('兴趣爱好', max_length=10)

    def __str__(self):
        return self.name.encode('utf8')


#class English(models.Model)


class Publication(models.Model):
    student=models.ForeignKey('Student')
    name=models.CharField('出版物名称', max_length=20)
    date=models.DateField('出版时间')
    #file=models.FileField('出版物封面', upload_to='/')

    def __str__(self):
        return self.name.encode('utf8')


class SpecialAward(models.Model):
    student=models.ForeignKey('Student')
    name=models.CharField('奖励名称', max_length=20)
    date=models.DateField('获奖日期')

    def __str__(self):
        return self.name.encode('utf8')


class Voluntary(models.Model):
    student=models.ForeignKey('Student')
    date=models.DateField('活动日期')
    activity=models.TextField('活动内容')
    result=models.TextField('活动成果')


