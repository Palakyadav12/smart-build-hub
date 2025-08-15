from django.urls import path
from . import views

urlpatterns=[
    path('contractordash/',views.contractordash,name='contractordash'),
    path('contractorchangepassword/',views.contractorchangepassword,name='contractorchangepassword'),
    path('contractorlogout/',views.contractorlogout,name='contractorlogout'),
    path('contractoredit/',views.contractoredit,name='contractoredit'),
    path('contractorprofile/',views.contractorprofile,name='contractorprofile'),
    path('contractorviewprojects/',views.contractorviewprojects,name='contractorviewprojects'),
    path('applyproject/<id>',views.applyproject,name='applyproject'),
    path('contractorapplications/',views.contractorapplications,name='contractorapplications'),
    path('assignedprojects/',views.assignedprojects,name='assignedprojects'),
    path('addprogress/<id>',views.addprogress,name='addprogress'),
]