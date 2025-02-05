from django.urls import path
from .views import EventListView, EventDetailView, MixedEventPromotionListView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<slug:slug>/', EventDetailView.as_view(), name='event-detail'),
    path('getMixedAllData/', MixedEventPromotionListView.as_view(), name='event-detail'),
]
