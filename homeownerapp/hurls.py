from django.urls import path
from . import views

urlpatterns=[


path('homeownerdash/',views.homeownerdash,name='homeownerdash'),
path('homeownerlogout/',views.homeownerlogout,name='homeownerlogout'),
path('homeownerchangepassword/',views.homeownerchangepassword,name='homeownerchangepassword'),
path('homeowneredit/',views.homeowneredit,name='homeowneredit'),
path('homeownerprofile/',views.homeownerprofile,name='homeownerprofile'),
path('addproject/',views.addproject,name='addproject'),
path('homeownerviewprojects/',views.homeownerviewprojects,name='homeownerviewprojects'),
path('homeownerviewapplications/<id>',views.homeownerviewapplications,name='homeownerviewapplications'),
path('rejectapp/<id>',views.rejectapp,name='rejectapp'),
path('approveapp/<id>',views.approveapp,name='approveapp'),
path('runningprojects/',views.runningprojects,name='runningprojects'),
path('viewupdates/<id>',views.viewupdates,name='viewupdates'),
path('homeownercompletedprojects',views.homeownercompletedprojects,name='homeownercompletedprojects'),
]