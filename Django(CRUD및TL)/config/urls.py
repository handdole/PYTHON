"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

import bookmark
import member
from bookmark import views as b_v
from member import views as m_v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/',bookmark.views.BookmarkListView.as_view(),name='list'),
    path('bookcreate/',b_v.BookCreate.as_view(),name='create'),
    path('bookupdate/<int:pk>',b_v.BookUpdate.as_view(),name='update'),
    path('bookdelete/<int:pk>',b_v.BookDelete.as_view(),name='delete'),
    path('bookdetail/<int:pk>', b_v.BookDetail.as_view(), name='detail'),
    # path('<str:id>/<str:pw>/',b_v.index),
    path('memberlist/',m_v.Member_List_View.as_view(),name='m_list'),
    path('membercreate/',m_v.Member_Create_View.as_view(), name='m_create'),
    path('memberupdate/<str:pk>',m_v.member_update_view.as_view(),name='m_update'),
    path('memberdetail/<str:pk>',m_v.member_detail_view.as_view(),name='m_detail'),
    path('memberdelete/<str:pk>',m_v.member_delete_view.as_view(),name='m_delete'),
]
