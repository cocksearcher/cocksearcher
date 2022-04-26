from rest_framework import serializers


class CocktailDetailSerializer(serializers.Serializer):
    name = serializers.CharField(allow_null=False)
    ingredients = serializers.ListField(child=serializers.CharField(allow_null=False))
    image_url = serializers.CharField(allow_null=False)
    recipe = serializers.ListField(child=serializers.CharField(allow_null=False))
    mood = serializers.CharField(allow_null=False)
    abv = serializers.FloatField(allow_null=False)
    likes = serializers.CharField(allow_null=False)
    is_liked = serializers.BooleanField(allow_null=False)
