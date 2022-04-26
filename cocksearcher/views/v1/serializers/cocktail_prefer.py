from rest_framework import serializers


class CocktailPreferSerializer(serializers.Serializer):
    id = serializers.CharField()
