from django.urls import path
from. import views

urlpatterns = [
path ('',views.lower,name='lower'),
path ('data_show/',views.lower_view,name='lower_data')
]