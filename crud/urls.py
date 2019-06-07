"""crud URL Configuration

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
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/layout', blog.views.layout, name='layout'),
    path('blog/home/', blog.views.home, name='home'),
    path('blog/new/', blog.views.new, name='new'),
    path('', blog.views.main, name='main'),
    path('blog/banner/', blog.views.banner, name='banner'),
    path('blog/create/', blog.views.create, name='create'),
    path('blog/newblog/', blog.views.blogform, name='newblog'),
    path('blog/<int:pk>/edit/', blog.views.edit, name='edit'),
    path('blog/<int:pk>/remove/', blog.views.remove, name='remove'),
    #comment
    path('blog/<int:blog_id>/comment/', blog.views.detail, name='comment'),
    path('blog/<int:blog_id>/comment_edit/<int:pk>/', blog.views.comment_edit, name='comment_edit'),
    path('blog/<int:blog_id>/comment_remove/<int:pk>/', blog.views.comment_remove, name='comment_remove'),
    #hashtag
    path('blog/hashtag/', blog.views.hashtagform, name='hashtag'),
    path('blog/<int:hashtag_id>/search/', blog.views.search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)