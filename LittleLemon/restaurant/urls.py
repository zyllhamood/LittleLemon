from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    #path('booking/',BookingViewSet.as_view()),
    path('menu/',MenuItemView.as_view()),
    path('menu/<int:pk>',SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]