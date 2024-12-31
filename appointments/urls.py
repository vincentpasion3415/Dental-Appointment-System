from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Main page
    path('book/', views.book_appointment, name='book_appointment'),  # Booking form
    path('success/', views.appointment_success, name='appointment_success'),  # Success page
    path('services/', views.services, name='services'),  # Services page
    path('about/', views.about, name='about'),  # About Us page
]
