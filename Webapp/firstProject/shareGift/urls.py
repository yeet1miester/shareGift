"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .import views  
urlpatterns = [
    path('', views.home, name= 'home'),
    path('aboutus/', views.about, name= 'AboutUs'),
    path('response/', views.response, name="response"),
    path('baekhyun/', views.baek, name="response"),
    path('branches/', views.branch, name="branch"),
    path('christmas/', views.christ, name="christ"),
    path('donate/', views.donate, name="donate"),
    path('mealtrain/', views.meal, name="meal"),
    path('pandemictimes/', views.pande, name="pande"),
    path('peertutoring/', views.peer, name="peer"),
    path('publications/', views.publica, name="publica"),
    path('seoul/', views.seoul, name="seoul"),
    path('singapore/', views.sing, name="sing"),
    path('dental/', views.dental, name ="dental"),
    path('deafandblind/',views.deaf,name="deafandblind"),
    path('individual/', views.indiv,name="individual"),
    path('ptimes/', views.ptimes, name ="ptimes"),
]
