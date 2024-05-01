
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView,UserBankAccountUpdateView,editPassword
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView, name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ),
    path('pass_change/', editPassword.as_view(), name='pass_change')
]