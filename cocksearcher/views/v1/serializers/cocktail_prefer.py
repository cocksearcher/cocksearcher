from rest_framework import serializers


class CocktailPreferSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    id = serializers.CharField()
