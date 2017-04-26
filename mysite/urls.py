from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from mysite.core import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    
    url(r'^landowner$',core_views.landowner, name='landowner'),
    
    url(r'^security$',core_views.security, name='security'),
    url(r'^security/vacate$',core_views.security_vacate, name='security_vacate'),
    url(r'^security/book$',core_views.security_book, name='security_book'),
    
    url(r'^carowner$', core_views.carowner, name='carowner'),
    url(r'^carowner/search$', core_views.search),
    # url(r'^carowner/search/place$', core_views.search),
    url(r'^carowner/search/place/(?P<place_name>([a-z]+))/$', core_views.search_place),
    url(r'^carowner/search/location/(?P<pin_code>([0-9]+))/$', core_views.search_location),
    
    url(r'^landowner/login/$', auth_views.login, {'template_name': 'login_landowner.html'}, name='login_landowner'),
    url(r'^carowner/login/$', auth_views.login, {'template_name': 'login_carowner.html'}, name='login'),
    url(r'^security/login/$', auth_views.login, {'template_name': 'login_security.html'}, name='login_security'),
    
    url(r'^landowner/logout/$', auth_views.logout, {'next_page': 'login_landowner'}, name='logout_landowner'),
    url(r'^carowner/logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^security/logout/$', auth_views.logout, {'next_page': 'login_security'}, name='logout_secrity'),
    
    url(r'^landowner/signup/$', core_views.signup_landowner, name='signup'),
    url(r'^carowner/signup/$', core_views.signup_carowner, name='signup_carowner'),
    
    url(r'^admin/', admin.site.urls),    	
]
