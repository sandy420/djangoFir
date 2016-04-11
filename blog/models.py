from django.db import models
from django.contrib import admin
import blog.deployee
from django import forms


# Create your models here.
class BlogPost(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


class BlogLog(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    logcreattime = models.DateTimeField()


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    length = models.IntegerField()


class Person(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    middle = models.CharField(max_length=100, blank=True)


class Login(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=100)
    creattime = models.DateTimeField()
    logintime = models.DateTimeField()
    loginIp = models.GenericIPAddressField(unpack_ipv4=True)
    isActive = models.NullBooleanField()


class Server(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    privateip = models.GenericIPAddressField()
    internetip = models.GenericIPAddressField()
    buytime = models.DateField()
    position = models.CharField(max_length=120)
    usecase = models.NullBooleanField()
    configurinfo = models.TextField()
    remark = models.TextField()

    def __str__(self):
        return self.buytime


class UserForm(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=120)
    headImg = models.FileField(upload_to='./upload/')

    def __str__(self):
        return self.username


class UploadFile(models.Model):
    filename = models.CharField(max_length=100)
    filepath = models.CharField(max_length=200)
    uploadtime = models.DateTimeField()

    def __str__(self):
        return self.filename
