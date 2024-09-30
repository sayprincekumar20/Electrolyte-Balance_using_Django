from django.urls import path
from .views import predict_electrolyte


urlpatterns = [
    path('', predict_electrolyte, name='predict_electrolyte'),
]


