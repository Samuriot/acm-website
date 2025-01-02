from django.urls import re_path as url
from django.urls import include
from AcmApp import views
from rest_framework.routers import DefaultRouter

from django.conf.urls.static import static
from django.conf import settings

# Create a router and register our ViewSets with it.

router = DefaultRouter()
router.register(r'members', views.MemberViewset, basename='member')
router.register(r'officers', views.OfficerViewset, basename='officer')
router.register(r'events', views.EventViewset, basename='event')
router.register(r'comments', views.CommentViewset, basename='comment')






# The API URLs are now determined automatically by the router.
urlpatterns = [
    url("api/", include(router.urls)),
    # url('members/', views.MemberViewset.as_view(), name='member'),
    # url('officers/', views.OfficerViewset.as_view(), name='officer'),
    # url('events/', views.EventViewset.as_view(), name='event'),
    # url('comments/', views.CommentViewset.as_view(), name='comment')
]




