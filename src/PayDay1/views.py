# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#import self as self
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.template.backends import django

from .forms import EmployeeRegistrationForm, ManagerRegistrationForm, EmpoyeeAuthenticationForm, \
    ManagerAuthenticationForm
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Timesheet, Employee, Manager, Job, Job_complete, User
from .serializers import TimesheetSerializer, EmployeeSerializer, ManagerSerializer, JobSerializer, \
    Job_completeSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.conf import settings
import datetime
from django.utils import timezone
from django.utils.timezone import localdate
from datetime import datetime
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


from django.http import HttpResponseRedirect

# Create your views here.


class TimesheetView(viewsets.ModelViewSet):
    queryset = Timesheet.objects.filter(user="123")
    serializer_class = TimesheetSerializer


class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self, email=None):
        man = get_object_or_404(Employee, user=self.request.user)

        queryset = Employee.objects.filter(user=self.request.user)
        return queryset


class ManagerView(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer

    def get_queryset(self, email=None):
        man = get_object_or_404(Manager, user=self.request.user)

        queryset = Manager.objects.filter(user=self.request.user)
        return queryset



class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class Job_completeView(viewsets.ModelViewSet):
    queryset = Job_complete.objects.all()
    serializer_class = Job_completeSerializer


def paydayhome_view(request):
    return render(request, "paydayhome.html")

def contact(request):
    return render(request, "contact.html")


def home_screen_view(request):
    current_user = request.user
    context = {}
    employees = User.objects.all()
    context['employees'] = employees

    if request.user.is_authenticated:
        return render(request, "home.html", context)
    else:
        return render(request, "paydayhome.html", context)
    return render(request, "managerhome.html", context)


def manager_home_screen_view(request):
    current_user = request.user

    context = {}
    managers = Manager.objects.all()
    context['managers'] = managers

    if request.user.is_manager:
        return render(request, "managerhome.html", context)
    return render(request, "home.html", context)


def managerregistration_view(request):
    context = {}
    if request.POST:
        form = ManagerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')  # How to get data from a valid form
            raw_password = form.cleaned_data.get('password1')
            manager = authenticate(email=email, password=raw_password)  # how to create the account
            login(request, manager)
            return redirect('managerhome.html')
        else:
            context['managerregistration_form'] = form
    else:  # GET request
        form = ManagerRegistrationForm()
        context['managerregistration_form'] = form
        return render(request, 'managerregistration.html', context)


def employeeregistration_view(request):
    context = {}
    if request.POST:
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')  # How to get data from a valid form
            raw_password = form.cleaned_data.get('password1')
            employee = authenticate(email=email, password=raw_password)  # how to create the account
            login(request, employee)
            return redirect('home.html')
        else:
            context['employeeregistration_form'] = form
    else:  # GET request
        form = EmployeeRegistrationForm()
        context['employeeregistration_form'] = form
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'paydayhome.html')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = EmpoyeeAuthenticationForm(request.POST)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")
    else:
        form = EmpoyeeAuthenticationForm()

    context['login_form'] = form
    return render(request, 'login.html', context)


def manlogin_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("managerhome.html")

    if request.POST:
        form = ManagerAuthenticationForm(request.POST)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("managerhome.html")
    else:
        form = ManagerAuthenticationForm()
    context['manlogin_form'] = form
    return render(request, 'manlogin.html', context)


def emp_timesheet_history_view(request):
    queryset = Job.objects.all()
    
    today = datetime.now().month
    time = Timesheet.objects.filter(user=request.user,
                                    date__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0))
    return render(request, 'emp_timesheet_history.html', {'time': time,'jobs':queryset})
   



def man_timesheet_history_view(request):
    today = datetime.now().month
    time = Timesheet.objects.filter(user=request.user,
                                    date__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0))
    return render(request, 'man_timesheet_history.html', {'time': time})


def timeseet_approval(request):
    man = request.user
    employee_list = Employee
    today = datetime.now().month
    time = Timesheet.objects.filter(user=request.user, date__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0))
    return render(request, 'emp_timesheet_history.html', {'time':time})

def get_jobs(request):
	queryset = Job.objects.all()
	
	return render(request, 'profile_list.html',{'jobs':queryset})


    

def get_timesheets(request):
    #get current manager
    man = request.user
    employee_lsit = Employee.objects.get(manager = man)
    #load in all timesheets for employees for the month
    all_sheets = []
    for emp in employee_lsit:
        timesheets = Timesheet.objects.get(employee_timesheet=emp, date_month=datetime.now.month, approved= False)
        all_sheets = all_sheets + timesheets
    if request.POST:
        for timesheet in all_sheets:
            #see if checked
            checked = request.POST.get("timesheet {} approved".format(timesheet.id))
            if checked:
                timsheet.approved = True
                timesheet.save()
    else:
        return render('emp_timesheet_history.html', {'timsheets': all_sheets})

@csrf_exempt

def add_job(request):
    if request.POST:
        #take in data and update
        print(request.POST.get("job_name"))
        new_job = Job.objects.create(job_name = request.POST.get("job_name"), rate_card = request.POST.get("rate_card"))
        #Redirect to the all jobs page
        return HttpResponseRedirect("getjobs")
    else:
        return render(request,'add_job.html')

class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
        queryset = Employee.objects.all()
        return Response({'profiles': queryset})


class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('profile-list')

# was giving an error: 'serializers' not defined

# class LoginSerializer(serializers.Serializer):
#    email = serializers.EmailField(
#        max_length=100,
#        style={'placeholder': 'Email', 'autofocus': True}
#    )
#    password = serializers.CharField(
#        max_length=100,
#        style={'input_type': 'password', 'placeholder': 'Password'}
#    )
#    remember_me = serializers.BooleanField()
