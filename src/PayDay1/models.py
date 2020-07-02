# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

# Create your models here.




class Job(models.Model):
    job_name    = models.CharField( max_length=20)
    rate_card   = models.IntegerField()

    def __str__(self):
        return self.job_name


class Job_complete(models.Model):
    YES = 'yes'
    NO = 'no'
    JOB_COMPLETE_CHOICES = [
        (YES, 'yes'),
        (NO, 'no'),
    ]

    job_status  = models.CharField(
    max_length = 3,
    choices= JOB_COMPLETE_CHOICES,
    default = ' '
    )
    job_name        = models.ForeignKey(Job)

    def __str__(self):
        return self.job_status

class MyUserManager(BaseUserManager):
    #Creating a user
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
                email=self.normalize_email(email),
            )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser (self, email,company_id=None, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            

            )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    email           = models.EmailField(max_length=60, unique = True, primary_key=True)
    company_id      = models.CharField(max_length=4, default=' ')
    is_manager      = models.BooleanField(default=False)
    is_employee     = models.BooleanField(default=True)
    date_joined     = models.DateTimeField(auto_now= True)
    last_login      = models.DateTimeField(auto_now= True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)    
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['company_id']

    objects = MyUserManager()


    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
    # The user is identified by their email address
        return self.email




class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    man_id_number   = models.CharField(primary_key=True, max_length=4, unique= True)
    first_name      = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)
    manager         = models.BooleanField(default=True)


    objects = MyUserManager()


    def __str__(self):
        return self.man_id_number



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    emp_id_number   = models.CharField(primary_key=True, max_length=4, unique= True)
    first_name      = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)


    objects = MyUserManager()




    manager       = models.ForeignKey(Manager, default='choose manager')

    def __str__(self):
        return self.emp_id_number




    

class Timesheet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    date                = models.DateField(default = timezone.now)
    hours_worked        = models.IntegerField()
    salary              = models.IntegerField(null=True)
    timesheet_approve   = models.BooleanField(default=False)
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    job                 = models.ManyToManyField(Job)

    @property
    def addhours(self):
        totalhours = 0
        for jobs in self.job.all():
            a = jobs
            totalhours = totalhours + (jobs.rate_card * self.hours_worked)
        return totalhours





