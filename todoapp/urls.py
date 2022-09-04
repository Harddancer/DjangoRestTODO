from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectModelViewSet,TodoModelViewSet

app_name = 'users'

router = DefaultRouter()
# router = SimpleRouter()
router.register('project', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]