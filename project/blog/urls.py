"""sb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import login, logout

from .views import *

urlpatterns = [
    url(r'^$', BlogView.as_view(), name='blog'),
    url(r'^subscribe/$', SubscribeView.as_view(), name='subscribe'),

    # 전체글보기
    url(r'^all/$', AllView.as_view(), name='all_post'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^tags/$', TagView.as_view(), name='tag_search'),
    url(r'^category/(?P<keyword>\w+)/$', CategoryView.as_view(), name='category_list'),

    # 게시글 상세
    url(r'^post/(?P<post_id>\d+)/$', PostView.as_view(), name='post'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),

    # 게시글 작성
    url(r'^write/$', login_required(WriteView.as_view()), name='write'),

    # 방명록
    url(r'^guestbook/$', GuestBookView.as_view(), name='guestbook'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)