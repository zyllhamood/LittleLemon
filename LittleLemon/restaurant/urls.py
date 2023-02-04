from django.urls import path
from .views import *

urlpatterns = [
    #path('booking/',BookingViewSet.as_view()),
    path('menu/',MenuItemView.as_view()),
    path('menu/<int:pk>',SingleMenuItemView.as_view())
]