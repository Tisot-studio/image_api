from rest_framework import serializers
from .models import *


class AllImagesSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Images
        fields = '__all__'
        



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'