from django.urls import path
from .views import SubscriptionView, CityView, SubsDetailView, subscribe, EditSubscription


urlpatterns = [
    path('', CityView.as_view(), name = 'index'),
    path('subs_detail/<uuid:pk>', SubsDetailView.as_view(), name ='subs_detail'),
    path('subs/', SubscriptionView.as_view(), name = 'subs'),
    path('subscribe/<option>/<uuid:id>', subscribe, name ='subscribe'),
    path('subs/<uuid:id>', EditSubscription, name ='subs_edit'),
]