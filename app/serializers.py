from rest_framework import serializers
from .models import Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['ecommerce_usage'] = instance.get_ecommerce_usage_display()
    #     representation['monthly_turnover'] = instance.get_monthly_turnover_display()
    #     representation['commission_requirement'] = instance.get_commission_requirement_display()
    #     return representation
    

class StatItemSerializer(serializers.Serializer):
    platform = serializers.CharField(max_length=20, required=False)
    turnover = serializers.CharField(max_length=20, required=False)
    commission = serializers.CharField(max_length=20, required=False)
    count = serializers.IntegerField()

class StatisticsSerializer(serializers.Serializer):
    ecommerce_usage = StatItemSerializer(many=True)
    monthly_turnover = StatItemSerializer(many=True)
    commission_requirement = StatItemSerializer(many=True)