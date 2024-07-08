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
        ecommerce_stats = Survey.objects.values('ecommerce_usage').annotate(count=Count('id'))
        turnover_stats = Survey.objects.values('monthly_turnover').annotate(count=Count('id'))
        commission_stats = Survey.objects.values('commission_requirement').annotate(count=Count('id'))
        
        ecommerce_mapping = dict(Survey.ECOMMERCE_CHOICES)
        turnover_mapping = dict(Survey.TURNOVER_CHOICES)
        commission_mapping = dict(Survey.COMMISSION_CHOICES)
        
        formatted_stats = {
            'ecommerce_usage': [
                {
                    'platform': ecommerce_mapping.get(stat['ecommerce_usage'], 'Unknown'),
                    'count': stat['count']
                }
                for stat in ecommerce_stats
            ],
            'monthly_turnover': [
                {
                    'turnover': turnover_mapping.get(stat['monthly_turnover'], 'Unknown'),
                    'count': stat['count']
                }
                for stat in turnover_stats
            ],
            'commission_requirement': [
                {
                    'commission': commission_mapping.get(stat['commission_requirement'], 'Unknown'),
                    'count': stat['count']
                }
                for stat in commission_stats
            ]
        }
        
        return Response(formatted_stats, status=status.HTTP_200_OK)
