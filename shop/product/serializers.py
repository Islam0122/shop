from rest_framework import serializers
from .models import Category,Tag, Product

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title","slug")
        read_only_fields = ("id","slug")

    def validate_tag_name(self, value):
        if len(value) > 3:
            raise serializers.ValidationError("Tag name is too long")
        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title","slug")
        read_only_fields = ("id","slug")

class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(),required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ("id", "title",
                  "description","price",
                  "image",
                  "tags","category",
                  "status","is_active",
                  "created","updated",)