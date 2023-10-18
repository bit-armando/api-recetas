from rest_framework.routers import DefaultRouter

from blogs.api.api import BlogViewSet

router = DefaultRouter()

router.register('', BlogViewSet, basename="blogs")

urlpatterns = router.urls