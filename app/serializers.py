from rest_framework import serializers
from .models import Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ecommerce_usage'] = instance.get_ecommerce_usage_display()
        representation['monthly_turnover'] = instance.get_monthly_turnover_display()
        representation['commission_requirement'] = instance.get_commission_requirement_display()
        return representation
    


class StatisticsSerializer(serializers.Serializer):
    platform = serializers.CharField(max_length=20)
    count = serializers.IntegerField()