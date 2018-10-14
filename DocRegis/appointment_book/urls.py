from appointment_book import views
from django.urls import path, include

from rest_framework import routers

app_name = 'Appointment_book'

router = routers.DefaultRouter()
router.register('', views.AppointmentViewSet, base_name='appointment')

urlpatterns = router.urls
