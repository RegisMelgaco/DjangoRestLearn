from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointments/', include('appointment_book.urls')),
    path('auth/', include('rest_auth.urls'))
]
