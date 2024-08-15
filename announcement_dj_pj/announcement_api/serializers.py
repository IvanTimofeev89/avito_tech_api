from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import Ad, AdPicture


class AdPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdPicture
        fields = ["link"]


class AdSerializer(serializers.ModelSerializer):
    pictures = AdPictureSerializer(many=True, label="Изображение", read_only=True, required=False)
    uploaded_pictures = serializers.ListField(
        child=serializers.ImageField(use_url=True, required=False),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Ad
        fields = ["id", "name", "price", "description", "pictures", "uploaded_pictures"]

    def create(self, validated_data):
        uploaded_pictures = validated_data.pop("uploaded_pictures")

        if len(uploaded_pictures) > 3:
            raise ValidationError("Максимальное количество фотографий - 3.")

        ad = Ad.objects.create(**validated_data)

        for picture in uploaded_pictures:
            AdPicture.objects.create(announcement=ad, link=picture)

        return ad


class AdListSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = ["name", "picture", "price"]

    def get_picture(self, obj):
        first_picture = obj.pictures.first()
        if first_picture:
            return first_picture.link.url
        return "Изображение отсутствует"


class AllFieldsListSerializer(serializers.ModelSerializer):
    pictures = AdPictureSerializer(many=True, label="Изображение", read_only=True)

    class Meta:
        model = Ad
        fields = ["name", "price", "description", "pictures"]
