from django.urls import path
from. import views

urlpatterns = [
path ('data/',views.ncase,name='ncase'),
path ('view/',views.case_view,name='case_view'),

path ('search/',views.search_case,name='search_case')

]