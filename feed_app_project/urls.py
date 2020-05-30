"""feed_app_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import feed.views
import django.contrib.auth.views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feed.views.Home_Page.as_view(), name='home_page'),
    path('newpost/', feed.views.New_Post.as_view(), name='new_post'),
    path('login/', feed.views.Login_View.as_view(), name='login_url'),
    path('logout/', django.contrib.auth.views.LogoutView.as_view(), name='logout_url'),
    path('post/<int:post_id>/', feed.views.Comments_View.as_view(), name='comments_url'),
    path('post/<int:post_id>/newcomment/', feed.views.New_Comment.as_view(), name='new_comment'),
    path('post/<int:post_id>/upvote', feed.views.upvote_post, name='upvote_url'),
]

#serving media files for development only
if settings.DEBUG:
    urlpatterns += static(prefix=settings.MEDIA_URL, view=serve, document_root=settings.MEDIA_ROOT)
    #https://docs.djangoproject.com/en/3.0/ref/views/#django.views.static.serve
    #https://docs.djangoproject.com/en/3.0/ref/urls/#django.conf.urls.static.static