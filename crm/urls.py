from django.urls import path
from . import views
from .views import (
    CompanyListView,CompanyDetailView,CompanyCreateView,CompanyUpdateView,CompanyDeleteView,
    ContactListView,ContactDetailView,ContactCreateView,ContactUpdateView,ContactDeleteView,
    QuarryListView,QuarryDetailView,QuarryCreateView,QuarryUpdateView,QuarryDeleteView)

urlpatterns = [
    path('', CompanyListView.as_view(), name='crm-home'),

    path('company/', CompanyListView.as_view(), name='crm-company'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('company/new/', CompanyCreateView.as_view(), name='company-create'),
    path('company/<int:pk>/update/', CompanyUpdateView.as_view(), name='company-update'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),

    path('contact/', ContactListView.as_view(), name='crm-contact'),
    path('contact/<int:pk>/',ContactDetailView.as_view(), name='contact-detail' ),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update/',ContactUpdateView.as_view(), name='contact-update' ),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),

    path('quarry/', QuarryListView.as_view(), name='crm-quarry'),
    path('quarry/<int:pk>/', QuarryDetailView.as_view(), name='quarry-detail'),
    path('quarry/new/', QuarryCreateView.as_view(), name='quarry-create' ),
    path('quarry/<int:pk>/update/',QuarryUpdateView.as_view(), name='quarry-update' ),
    path('quarry/<int:pk>/delete/', QuarryDeleteView.as_view(), name='quarry-delete'),

    path('contact_details/', views.person, name='crm-person'),


]
