from django.contrib import admin
from django.urls import path, include

import accounts.urls
from insta import views
import insta.urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('insta/', include(insta.urls)),
    path('accounts/',include(accounts.urls)),
    path('',insta.views.selectAll,name="start"),
]

from django.conf.urls.static import *
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)