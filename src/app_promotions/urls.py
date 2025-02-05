from django.urls import path
from .views import PromotionListView, PromotionDetailView

urlpatterns = [
    path('offers/', PromotionListView.as_view(), name='promotion-list'),
    path('offers/<slug:slug>/', PromotionDetailView.as_view(), name='promotion-detail'),
]
