from django.urls import path
from . import views

urlpatterns = [
    path('app/sample/', views.sample_get_view, name='sample_get_view'),
    path('app/sample1/', views.sample1, name='sample1'),
    path('app/tharun/', views.tharun, name='tharun'),  # First 'tharun' route
    path('app/tharun1/', views.tharun1, name='tharun1'),  # Changed to 'tharun1' for uniqueness
]
