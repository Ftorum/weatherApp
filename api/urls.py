from django.urls import path
from .views import SubsAPIView, CityAPIView, city_create, city_delete,city_update
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('', SubsAPIView.as_view(), name='subs_list'),
    path('city', CityAPIView.as_view(), name='cities_list'),
    path('city/create', city_create, name='create'),
    path('city/delete/<uuid:pk>', city_delete, name='delete'),
    path('city/update/<uuid:pk>', city_update, name='update'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]