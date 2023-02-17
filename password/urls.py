from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('accounts/signup', SignUpView.as_view(), name='signup'),
    path('add-password', PasswordCreateView.as_view(), name='add')
]