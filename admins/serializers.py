from rest_framework import serializers
from .models import userAdmin

class Adminserializer(serializers.ModelSerializer):
    class Meta:
        model = userAdmin
        fields = '__all__'

class updateAdminserializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = userAdmin
        fields = '__all__'