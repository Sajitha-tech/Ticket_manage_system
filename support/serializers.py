from rest_framework import serializers
from support.models import User

class UserSeriaizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","phone","password"]
        read_only_fields=["id"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","phone","password"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)