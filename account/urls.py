
from django.urls import path

from account.views import RegisterView, CustomLoginView

urlpatterns = [
    path('register_view', RegisterView.as_view(), name='register_view'),
    path('login_view', CustomLoginView.as_view(), name='login_view'),
]
