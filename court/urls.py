from django.urls import path
from. import views

urlpatterns = [
path ('',views.court_view,name='court_view'),
path ('data/',views.court_data,name='court'),
]