from rest_framework import serializers


class IngredientDetailSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(allow_null=False)
    image_url = serializers.CharField(allow_null=False)
