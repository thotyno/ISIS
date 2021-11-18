from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('cs', views.cs, name='cs'),
    path('cs/mark', views.csmark, name='csmark'),
    path('cs/teacher', views.teacher, name='teacher'),
    path('cs/tkb/all', views.tkball, name='tkball'),
    path('cs/tkb/class', views.tkbclass, name='tkbclass'),
    path('cs/noti/all', views.noticlass, name='noticlass'),
    path('cs/noti/class', views.noticlass, name='noticlass'),
    path('cs/noti/user', views.noticlass, name='noticlass'),
    path('cs/sdb', views.sdb, name='sdb'),
    path('cs/tncs', views.tncs, name='tncs'),
    path('cs/class/map', views.classmap, name='classmap'),
    path('cs/class/bill', views.classbill, name='classbill'),
    path('cs/class/chat', views.classchat, name='classchat'),
    path('cs/class/mem', views.classmem, name='classmem'),
    path('personal', views.personal, name='personal'),
    path('personal/info', views.personalinfo, name='personalinfo'),
    path('schools', views.schools, name='schools'),
    path('schools/1', views.schools1, name='schools1'),
    path('wj', views.wj, name='wj'),
    path('wj/top', views.wjtop, name='wjtop'),
    path('wj/best', views.best, name='best'),
    path('nap', views.nap, name='nap'),
    path('lbr', views.lbr, name='lbr'),
    path('lh', views.lh, name='lh'),
    path('lal', views.lal, name='lal'),
    path('muvic', views.muvic, name='muvic'),

    path('fl', views.fl, name='fl'),
    path('nl', views.nl, name='nl'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('settings', views.settings, name='settings'),
    
]