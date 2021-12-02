"""CRMtool URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from leads.views import LandingPageClassView, UserCreateClassView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView, 
                                        PasswordResetDoneView, PasswordResetConfirmView,
                                        PasswordResetCompleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads')),
    path('', LandingPageClassView.as_view(), name='landing_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('singup/', UserCreateClassView.as_view(), name='singup'),
    path('agents/', include('agents.urls', namespace='agents')),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset' ),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/complete', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
