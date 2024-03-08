from django.urls import path
from .views import CustomerListView, HelperListView

urlpatterns = [
    path('customer/', CustomerListView.as_view(), name='customer-list'),
    path('helper/', HelperListView.as_view(), name='helper-list'),
]
