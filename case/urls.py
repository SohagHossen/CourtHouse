from django.urls import path
from. import views

urlpatterns = [
path ('',views.case,name='case'),
path ('status/',views.case_status,name='case_status')
]