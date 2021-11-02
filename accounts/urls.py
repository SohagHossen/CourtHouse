from django.urls import path
from. import views

urlpatterns = [
path ('',views.login,name='login'),
path ('registrations/',views.registrations,name='registrations'),
path('logout/', views.logout, name='logout'),
]