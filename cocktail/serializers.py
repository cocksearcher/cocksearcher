from rest_framework import serializers


class IngredientDetailSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(allow_null=False)
    image_url = serializers.CharField(allow_null=False)


class CocktailDetailSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(allow_null=False)
    ingredients = serializers.ListField(child=IngredientDetailSerializer())
    image_url = serializers.CharField(allow_null=False)
    recipe = serializers.ListField(child=serializers.CharField(allow_null=False))
    mood = serializers.CharField(allow_null=False)
    abv = serializers.FloatField(allow_null=False)
    likes = serializers.CharField(allow_null=False)
    is_liked = serializers.BooleanField(allow_null=False)


class CocktailPreferSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    id = serializers.CharField()
