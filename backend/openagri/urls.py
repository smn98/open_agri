from django.urls import path
from django.contrib import admin
from users import views as users_views
from devices import views as devices_views
from mobile import views as mobile_views
from weatherStation import views as weather_views
from qgis import views as qgis_views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users import serializers as user_serializers

router = routers.DefaultRouter()

router.register(r'users', users_views.UserViewSet, basename='user')
router.register(r'devices', devices_views.DeviceViewSet, basename='device')
router.register(r'mobiles', mobile_views.MobileViewSet, basename='mobile')
router.register(r'crops', mobile_views.CropViewSet, basename='crop')
router.register(r'images', devices_views.ImageViewSet, basename='image')
router.register(r'qgis', qgis_views.QGISViewSet, basename='qgis')
router.register(r'wstations', weather_views.WeatherStationViewSet, basename='wstation')
router.register(r'wstations-edge', weather_views.WeatherStationAPIkeyViewSet, basename='wstation-edge')
router.register(r'api-keys', users_views.ApiKeyViewSet, basename='api-key')

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(serializer_class=user_serializers.CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]