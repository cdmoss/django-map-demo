from rest_framework import routers
from .api import PlaceViewSet

router = routers.DefaultRouter()
router.register('api/places', PlaceViewSet, 'places')

urlpatterns = router.urls
