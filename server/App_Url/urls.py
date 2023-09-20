from django.urls import path

# jwt token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from App_Account.views import UserViewsets
# App_Order views
from App_Order.views import CustomerDetailViewset, OrderViewsets, IngredientViewset


from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'user', UserViewsets, basename='user')
router.register(r'order', OrderViewsets, basename='order')
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+router.urls
