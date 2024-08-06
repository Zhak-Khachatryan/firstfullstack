from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', CreateUserView.as_view(), name = 'register'),
    path('token/', TokenObtainPairView.as_view(), name = 'token'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'refresh'),
    path('api-auth/', include('rest_framework.urls')),
]
