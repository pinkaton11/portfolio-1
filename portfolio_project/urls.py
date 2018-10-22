"""portfolio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.contrib import admin

import portfolio.views as portfolio_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^portfolio/', portfolio_view.Portfolio.as_view()),
    url(r'^loginPortfolio/', portfolio_view.loginPortfolio, name='login_portfoliio'),
    url(r'^portfolio_page/', portfolio_view.Portfolio_Page.as_view()),
    url(r'^portfolio_page_sub/', portfolio_view.Portfolio_Page_Sub.as_view()),
    url(r'^about/', portfolio_view.About.as_view()),
    url(r'^about_sub/', portfolio_view.About_Sub.as_view()),
    url(r'^skills/', portfolio_view.Skills.as_view()),
    url(r'^skills_sub/', portfolio_view.Skills_Sub.as_view()),
    url(r'^calender/', portfolio_view.Calender.as_view()),
    url(r'^calender_sub/', portfolio_view.Calender_Sub.as_view()),
    url(r'^getschedule/', portfolio_view.getSchedule, name='get_schedule'),
    url(r'^saveschedule/', portfolio_view.saveSchedule, name='save_schedule'),
    url(r'^deleteschedule/', portfolio_view.deleteSchedule, name='delete_schedule'),
    url(r'^excreater/', portfolio_view.ExCreater.as_view()),
    url(r'^tools/', portfolio_view.Tools.as_view()),
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
