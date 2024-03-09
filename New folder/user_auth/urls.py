from django.urls import path
from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('login_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('signup/', views.UserSignupView.as_view(), name='user-signup'),
    path('rest_login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
