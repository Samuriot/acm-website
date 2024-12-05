from django.urls import re_path as url
from AcmApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^member$', views.memberApi),
    url(r'^member/([0-9]+)$', views.memberApi),

    url(r'^officer$', views.officerApi),
    url(r'^officer/([0-9]+)$', views.officerApi),

    url(r'^event$', views.eventApi),
    url(r'^event/([0-9]+)$', views.eventApi),

    url(r'^comment$', views.commentApi),
    url(r'^comment/([0-9]+)$', views.commentApi),

    url(r'^/member/savefile', views.SaveFile)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


