from rest_framework import serializers
from musicDetails.models import Activity, Performance

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'  # 將所有欄位都包含在序列化結果中

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'  # 將所有欄位都包含在序列化結果中