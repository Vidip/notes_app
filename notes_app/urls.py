"""notes_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from notes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/', views.notes_profile, name='notes_profile'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^add_note/', views.add_note, name='add_note'),
    url(r'^delete_note/(?P<note_id>[0-9]+)', views.delete_note, name='delete_note'),
    url(r'^open_note/(?P<note_id>[0-9]+)', views.open_note, name='open_note'),
    url(r'^share_note/(?P<note_id>[0-9]+)', views.share_note, name='share_note'),
    url(r'^share_note_to_user/(?P<note_id>[0-9]+)', views.share_note_to_user, name='share_note_to_user'),
    url(r'^mark_note/(?P<note_id>[0-9]+)', views.mark_note, name='mark_note'),
    #url(r'^chat/', include('chat.urls')),
    url(r'^admin/',admin.site.urls),
]