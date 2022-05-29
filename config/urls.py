from django.contrib import admin
from django.urls import path, include
from .views import api_gate_way_response

app_name = "config"

urlpatterns = [
    # api gateway
    path("", api_gate_way_response),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name="api"),
]
