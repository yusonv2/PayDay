from django.conf.urls import url, include
from . import views
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from .views import employeeregistration_view, managerregistration_view, logout_view, login_view, manlogin_view, paydayhome_view, emp_timesheet_history_view



router = routers.DefaultRouter()
router.register('Timesheet', views.TimesheetView, 'timesheet')
router.register('Employee', views.EmployeeView, basename="Employee")
router.register('Manager', views.ManagerView, basename="Manager")
router.register('Job', views.JobView, basename="Job")
router.register('Job_complete', views.Job_completeView, basename="Job_complete")


urlpatterns = [
	url('', include(router.urls)),
	url(r'^paydayhome', views.paydayhome_view, name='paydayhome'),
	url(r'^home', views.home_screen_view, name='home'),
	url(r'^managerhome', views.manager_home_screen_view, name='managerhome'),
	url(r'^empregister$', views.employeeregistration_view, name='register'),
	url(r'^manregister$', views.managerregistration_view, name='manregister'),
	url(r'^logout$', views.logout_view, name='logout'),
	url(r'^login$', views.login_view, name='login'),
	url(r'^manlogin$', views.manlogin_view, name='manlogin'),
	url(r'^emp_timesheet_history$', views.emp_timesheet_history_view, name='emp_timesheet_history'),
	url(r'^man_timesheet_history$', views.man_timesheet_history_view, name='man_timesheet_history'),
	url(r'getjobs', views.get_jobs, name='get_jobs'),
	url(r'add_job', views.add_job, name='add_job'),
	url(r'^contact.html$', views.contact, name='contact'),

]
