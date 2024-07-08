from rest_framework import viewsets
from .models import Survey
from .serializers import SurveySerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import Survey
from .serializers import StatisticsSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer




class StatisticsView(APIView):
    def get(self, request):
        statistics = Survey.objects.values('ecommerce_usage').annotate(count=Count('id'))
        
        platform_mapping = {
            'a': 'Telegram',
            'b': 'Instagram',
            'c': 'Facebook',
            'd': 'E-commerce',
            'e': 'Yoq'
        }
        
        formatted_statistics = [
            {
                'platform': platform_mapping.get(stat['ecommerce_usage'], 'Unknown'),
                'count': stat['count']
            }
            for stat in statistics
        ]
        
        serializer = StatisticsSerializer(formatted_statistics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)