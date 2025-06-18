from django.urls import path
from .views import ExplanationView


urlpatterns = [
    path('exp/', ExplanationView.as_view(), name='explanation'),
]