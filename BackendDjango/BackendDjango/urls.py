from django.urls import path
from myBackend.views import RegisterUserView, VerifyEmailView, SetPasswordView, GenerateWinnerView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('set-password/', SetPasswordView.as_view(), name='set-password'),
    path('generate-winner/', GenerateWinnerView.as_view(), name='generate-winner'),
    
]
