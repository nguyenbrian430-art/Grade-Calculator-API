
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ClassViewSet,AssignmentViewSet

router = routers.DefaultRouter()
router.register("class", ClassViewSet)
router.register("assignment", AssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
