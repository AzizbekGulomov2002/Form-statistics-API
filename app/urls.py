
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet,StatisticsView

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]