from django.urls import path
from. import views

urlpatterns = [
path ('',views.police,name='police'),
path ('data/',views.police_view,name='police_data')
]