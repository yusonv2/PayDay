# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Timesheet, Manager, Job, Job_complete, Employee, User

admin.site.register(Timesheet)
admin.site.register(Manager)
admin.site.register(Job)
admin.site.register(Job_complete)
admin.site.register(Employee)
admin.site.register(User)

