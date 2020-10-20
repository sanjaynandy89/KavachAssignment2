from rest_framework import serializers
from kavachapi.models import Test
class KavachApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['testdata']