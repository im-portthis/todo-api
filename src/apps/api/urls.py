from django.urls import path, include
from apps.api.v1.router import router as router_v1

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('', include(router_v1.urls)),
]
