from rest_framework import serializers


class IngredientDetailSerializer(serializers.Serializer):
    name = serializers.CharField(allow_null=False)
    image_url = serializers.CharField(allow_null=False)
