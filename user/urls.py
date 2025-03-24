from django.urls import path
from .views import RegisterUserView,GetEmailTokenView

urlpatterns = [
    path('register/',RegisterUserView.as_view(),name='register'),
    path('login/',GetEmailTokenView.as_view(),name='token')
]
