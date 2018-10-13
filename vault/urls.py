from django.conf.urls import include, url
import vault.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^account/$', vault.views.account, name='account'),
    url(r'^login$', auth_views.login, {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'logout.html', 'next_page': '/'}, name='logout'),
    url(r'^account/change_password$', auth_views.password_change,
        {'template_name': 'password_change.html'}, name='password_change'),
    url(r'^account/change_password_done$', auth_views.password_change_done,
        {'template_name': 'password_change_done.html'},
        name='password_change_done'),
    url(r'^register/$', vault.views.register, name='register'),
]
