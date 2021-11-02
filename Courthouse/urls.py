
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('Home/', include('Home.urls')),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('judge/',include('judge.urls')),
    path('case/',include('case.urls')),
    path('lower/',include('lower.urls')),
    path('police/',include('police.urls')),
    path('Ncase/', include('Ncase.urls')),
    path('court/', include('court.urls')),

]
