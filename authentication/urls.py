from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from authentication.views import (
    RegistrationAPIView,
    RegistrationConfirmationAPIView,
    LoginUsingPhoneAPIView,
    LoginUsingPhoneConfirmationAPIView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('registration/confirmation/', RegistrationConfirmationAPIView.as_view(),
         name='registration_confirmation'),
    path('login/', LoginUsingPhoneAPIView.as_view(), name='login'),
    path('login/confirmation/', LoginUsingPhoneConfirmationAPIView.as_view(),
         name='login_confirmation'),
]
