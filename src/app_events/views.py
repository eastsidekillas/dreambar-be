from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from django.db.models import Q

from .models import Event
from app_promotions.models import Promotion
from app_promotions.serializers import PromotionSerializer
from .serializers import EventSerializer


class EventListView(APIView):
    def get(self, request):
        events = Event.objects.filter(status='published')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventDetailView(APIView):
    def get(self, request, slug):
        try:
            event = Event.objects.get(slug=slug, status='published')
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response({'error': 'Событие не загрузилось или не published'}, status=status.HTTP_404_NOT_FOUND)


class MixedEventPromotionListView(APIView):
    def get(self, request):
        events = Event.objects.filter(status='published')
        promotions = Promotion.objects.all()

        event_serializer = EventSerializer(events, many=True, context={'request': request})
        promotion_serializer = PromotionSerializer(promotions, many=True, context={'request': request})

        mixed_data = []

        for event in event_serializer.data:
            event['isPromotion'] = False
            mixed_data.append(event)

        for promotion in promotion_serializer.data:
            promotion['isPromotion'] = True
            mixed_data.append(promotion)

        random.shuffle(mixed_data)

        return Response(mixed_data, status=status.HTTP_200_OK)
