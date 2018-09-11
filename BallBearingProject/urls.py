"""BallBearingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from BallbearingSite import views

from django.conf.urls.static import static
from django.conf import settings
from ajax_select import urls as ajax_select_urls

urlpatterns = [
    # url(r'^$index',views.index,name='index'),
    url(r'^$',views.homepage,name='homepage'),
    url(r'^ajax_select/', include(ajax_select_urls)),
    url(r'^admin/BallbearingSite/controlsite/$',views.sendemailview),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('BallbearingSite.urls', namespace='BallbearingSite')),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
     url('^', include('django.contrib.auth.urls')),
    # url(r'^register/',views.RegistrationForm_view,name='register_form'),
   ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    # url(r'^BallbearingSite/',include(BallbearingSite.urls,namespace='BallbearingSite'))

admin.site.site_header = 'مدیریت'
admin.site.site_title = 'مدیریت'
