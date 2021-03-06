# -*- coding: utf-8 -*-
"""word_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve

import xadmin
from learn.views import LearningOverviewView

from users.views import LoginView, LogoutView, \
    RegisterView, AcivateUserView, ForgetPasswordView, ResetPasswordView, ModifyPasswordView, RegisterMobileView, \
    UserVirificationSmsView, VerifySmsView
from django.conf import settings

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$',  serve, {"document_root":settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$',  serve, {"document_root":settings.STATIC_ROOT}),
    url(r'^$', LearningOverviewView.as_view(), name="index"),
    url(r'^accounts/login/$', LoginView.as_view(), name="user_login"),
    url(r'^accounts/logout/$', LogoutView.as_view(), name="user_logout"),
    url(r'^register/$', RegisterView.as_view(), name="user_register"),
    url(r'^register_mobile/$', RegisterMobileView.as_view(), name="user_register_mobile"),
    url(r'^send_verification_sms/$', UserVirificationSmsView.as_view(), name="user_verification_sms"),
    url(r'^forget_password/$', ForgetPasswordView.as_view(), name="forget_password"),
    url(r'^forget_password_verify_sms/$', VerifySmsView.as_view(), name="verify_sms"),
    url(r'^reset_password/(?P<activate_code>.*)/$', ResetPasswordView.as_view(), name="reset_password"),
    url(r'^modify_password/$', ModifyPasswordView.as_view(), name="modify_password"),
    url(r'^activate/(?P<activate_code>.*)/$', AcivateUserView.as_view(), name="user_active"),
    url(r'^op/', include('operations.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^learn/', include('learn.urls')),
    url(r'^testings/', include('testings.urls')),
]


handler404 = 'word_master.views.handler404'
handler500 = 'word_master.views.handler500'