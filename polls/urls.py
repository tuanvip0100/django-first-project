from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<user_id>[0-9]+)/name/$', views.user_name, name='user_name'),
    url(r'^su/([0-9]+)/$', views.user_name),
    url(r'^sudo/<int:year>/$', views.user_name),
    url(r'^post/$', views.post_form),
    url(r'^post/1/$', views.get_name),
    url(r'^login/$', views.login_page),
    url(r'^login/request/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^get/detail/$', views.get_detail),
    url(r'^change/name/view/$', views.change_user_name_view),
    url(r'^change/name/$', views.change_user_name),
    url(r'^sign/view/$', views.sign_in_view),
    url(r'^sign/$', views.sign_in),
    url(r'^get/all/$', views.get_all_person),
    url(r'^delete/(?P<user_id>[0-9]+)/$', views.delete_person)
]
