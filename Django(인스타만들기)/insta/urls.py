from django.contrib import admin
from django.urls import path

import insta.views

urlpatterns = [
    path('test',insta.views.test,name='test'),
    path("upload", insta.views.PhotoUpload.as_view(), name="upload"),
    path("selectOne/<int:pk>", insta.views.SelectOne.as_view(), name="selectOne"),
    path("selectAll", insta.views.selectAll, name = "selectAll"),
]
