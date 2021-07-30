#Localized URL for myapi end
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'points', views.PointsConnectorViewSet)

#Login URLs accessed at end points of our API
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework') )
]