from django.urls import path

from App_Account.views import UserViewsets
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'user', UserViewsets, basename='user')
urlpatterns = [

]+router.urls
