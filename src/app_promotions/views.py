from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Promotion
from .serializers import PromotionSerializer


class PromotionListView(APIView):
    def get(self, request):
        promotions = Promotion.objects.filter(status='published')
        serializer = PromotionSerializer(promotions, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PromotionDetailView(APIView):
    def get(self, request, slug):
        try:
            promotion = Promotion.objects.get(slug=slug, status='published')
            serializer = PromotionSerializer(promotion, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Promotion.DoesNotExist:
            return Response({"error": "Акция не загрузилась или не published"}, status=status.HTTP_404_NOT_FOUND)
