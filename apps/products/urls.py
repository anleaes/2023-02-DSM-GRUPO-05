from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'products'

router = routers.DefaultRouter()
router.register('produtos', views.ProductViewSet, basename='produtos')

urlpatterns = [
    path('', include(router.urls) )
]
