from django.urls import path
from. import views

urlpatterns = [
path ('',views.Judge,name="judge"),
path ('data/',views.judge_view,name="judge_data")
]