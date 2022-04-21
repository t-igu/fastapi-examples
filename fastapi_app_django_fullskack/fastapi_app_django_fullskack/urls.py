"""fastapi_app_django_fullskack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import include, path              #includeを追加
from django.views.generic import TemplateView      #追加
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  #追加
    path('uikit/', TemplateView.as_view(template_name='uikit/index.html'), name='uikit'),  #追加
    path('index/', login_required(TemplateView.as_view(template_name='index.html')), name='index'),  #追加
    path('aggrid/', login_required(TemplateView.as_view(template_name='aggrid.html')), name='aggrid'),  #追加
    path('jexcel/', login_required(TemplateView.as_view(template_name='jexcel.html')), name='jexcel'),  #追加
    path('employee/', include('employee.urls')),                              #追加
    path('fileupload/', login_required(TemplateView.as_view(template_name='fileupload.html')), name='fileupload'),  #追加
    path('selectbox/', login_required(TemplateView.as_view(template_name='selectbox.html')), name='selectbox'),  #追加
    path('accounts/', include('allauth.urls')),                              #追加
]

