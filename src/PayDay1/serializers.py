from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Timesheet, Manager, Job, Job_complete, Employee

class TimesheetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Timesheet
        fields = (
            'date',
            'hours_worked',
            'job',
            'user',
                  )


class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Employee
        fields = ('user',
            'emp_id_number',
            'first_name',
            'last_name',
            'manager')


class ManagerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Manager
        fields = ('user',
            'man_id_number',
            'first_name',
            'last_name',
            )

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('job_name',
            'rate_card',)

class Job_completeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_complete
        fields = ('job_status',
            'job_name',)
