from rest_framework.routers import DefaultRouter
from users.api.views import UserModelViewSet

router_users = DefaultRouter()
router_users.register(prefix='users', viewset=UserModelViewSet, basename='users')
