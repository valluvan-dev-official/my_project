"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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


from django.contrib import admin
from django.urls import path
from my_application import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name = "home_main"),
    path("show/",views.display,name ="show"),
    path("jinja/",views.Jinja_view,name="jinja"),
    path("home/",views.extends_view,name="home"),
    path("regroup/",views.regroup_jinja,name="regroup"),
    path("login/",views.html_form,name="login"),
    path("django_form/",views.django_normal_form,name="django_form"),
]
