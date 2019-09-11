from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='crm-home'),
    path('company/', views.company, name='crm-company'),
    path('quarry/', views.quarry, name='crm-quarry'),
    path('contact/', views.contact, name='crm-contact'),
    path('person/', views.person, name='crm-person')
]
