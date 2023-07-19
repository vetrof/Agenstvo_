from rest_framework import serializers
from main.models import Realty, Gallery, Manager, Category
from zayavki.models import Zayavka


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['image', ]


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['name', 'phone', 'email', 'img']


class RealtySerializer(serializers.ModelSerializer):
    images = GallerySerializer(many=True, read_only=True)
    person = ManagerSerializer(read_only=True)

    class Meta:
        model = Realty
        fields = ['id', 'title', 'info', 'price', 'cat', 'person', 'img', 'email', 'images']


class ZayavkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zayavka
        fields = ['id', 'name', 'email', 'question', 'manager_id']


class AllCategories(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
