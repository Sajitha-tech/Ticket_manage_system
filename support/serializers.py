from rest_framework import serializers
from support.models import User,Ticket,TicketComment

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
    

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields="__all__"
        read_only_fields=['id','created_by','created_at','updated_at',]

    def validate_assigned_to(self, value):
        if value and not value.is_staff:
            raise serializers.ValidationError("Tickets can only be assigned to staff members.")
        return value

class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=TicketComment
        fields="__all__"
        read_only_fields=["id", "user", "ticket", "created_at"]

    

    