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




from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import Survey
from .serializers import SurveySerializer, StatisticsSerializer

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class StatisticsView(APIView):
    def get(self, request):
        ecommerce_stats = dict(Survey.objects.values('ecommerce_usage').annotate(count=Count('id')).values_list('ecommerce_usage', 'count'))
        turnover_stats = dict(Survey.objects.values('monthly_turnover').annotate(count=Count('id')).values_list('monthly_turnover', 'count'))
        commission_stats = dict(Survey.objects.values('commission_requirement').annotate(count=Count('id')).values_list('commission_requirement', 'count'))

        ecommerce_mapping = dict(Survey.ECOMMERCE_CHOICES)
        turnover_mapping = dict(Survey.TURNOVER_CHOICES)
        commission_mapping = dict(Survey.COMMISSION_CHOICES)

        formatted_stats = {
            'ecommerce_usage': [
                {
                    'platform': ecommerce_mapping.get(choice[0], 'Unknown'),
                    'count': ecommerce_stats.get(choice[0], 0)
                }
                for choice in Survey.ECOMMERCE_CHOICES
            ],
            'monthly_turnover': [
                {
                    'turnover': turnover_mapping.get(choice[0], 'Unknown'),
                    'count': turnover_stats.get(choice[0], 0)
                }
                for choice in Survey.TURNOVER_CHOICES
            ],
            'commission_requirement': [
                {
                    'commission': commission_mapping.get(choice[0], 'Unknown'),
                    'count': commission_stats.get(choice[0], 0)
                }
                for choice in Survey.COMMISSION_CHOICES
            ]
        }

        return Response(formatted_stats, status=status.HTTP_200_OK)

