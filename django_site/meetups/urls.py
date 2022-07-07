from django.urls import path
from . import views

urlpatterns = [
    path('meetup/', views.index, name='all-meetups'), # our-domain.com/meetups
    path('meetup/success', views.confirm_registration, name='confirm-registration'),
    path('meetup/<slug:meetup_slug>', views.meetup_details, name='meetup-details'), # our-domain.com/meetup/a-first-meetup or a-second-meetup ( dynamic-path-segment )
]
