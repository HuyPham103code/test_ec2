from django.urls import path
from .views import ChurnPredictionView, home

urlpatterns = [
    path('predict/', ChurnPredictionView.as_view(), name='ChurnPredictionView'),
    path('', home, name='Homepage'),
]