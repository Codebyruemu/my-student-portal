from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.register_student, name='student'),
    path('payment/<int:student_id>/', views.start_payment, name='start_payment'),
    path('success/', views.payment_success, name='success'),
    path('dashboard/', views.dashboard, name='dashboard'),
]