from django.conf.urls import url
from BallbearingSite import views
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page
from dal import autocomplete
from django.conf.urls import *
from django.contrib.auth.views import password_reset
app_name= 'BallbearingSite'

urlpatterns=[
url(r'^index/$',views.index,name='index'),
url(r'^sellerstocks/(?P<username>[\w.@+-]+)/$',views.allstocks_view,name='sellerstocks'),
# url(r'^buyerstocks/$',views.buyerstocks_view,name='buyerstocks'),
url(r'^excelfile/$',views.ca_import,name='excelfile'),
url(r'^news/$',views.news,name='news'),
url(r'^register/$',views.register,name='register'),
url(r'^BallbearingSite/user_login/$',views.user_login,name='user_login'),
url(r'^stock/$',views.stock,name='stock'),
url(r'^stock_autocomplete/$',views.StocksAutocomplete.as_view(create_field='carname'),name='stock_autocomplete'),
# url(r'^mystocks/(?P<id>\d+)$',views.stock_delete,name='delete'),
url(r'^mystocks/$',views.mystocks_view,name='mystocks'),
url(r'^mydesktop/$',views.mydesktop_view,name='mydesktop'),
url(r'^stock/(?P<id>\d+)$',views.stock_update,name='update'),
url(r'^(?P<id>\d+)$',views.detailnewsview,name='detail'),
url(r'^detailadvertisement/(?P<id>\d+)$',views.detailadvertisementsview,name='detailadvertisement'),
url(r'^login/$',views.user_login,name='login'),
url(r'^contact/$',views.ContactUsView,name='contact'),
# url(r'^search/$', views.search, name="search"),

# url(r'^password_reset/$', auth_views.password_reset, name='password_reset'), # this line use the default django password_reset template
url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'BallbearingSite/password_reset.html'}), #I replace this insted of above url inorder to change the template and set my password_reset template instedad
# url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'BallbearingSite/password_reset_done.html'}),
url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
# url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#                   auth_views.password_reset_confirm, {'template_name': 'BallbearingSite/password_reset_confirm.html'}),
# url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
url(r'^reset/done/$', auth_views.password_reset_complete,{'template_name': 'BallbearingSite/password_reset_complete.html'}),
]
