from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index , name= 'index'),
    path('settings', views.settings , name= 'settings'),
    path('upload', views.upload , name= 'upload'),
    path('search', views.search , name= 'search'),
    path('Profile/<str:pk>', views.Profile , name= 'Profile'),
    path('follow', views.follow , name= 'follow'),
    path('like-post', views.like_post , name= 'like-post'),    
    path('signup', views.signup , name= 'signup'),
    path('signin', views.signin , name= 'signin'),
    path('logout', views.logout , name= 'logout'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)