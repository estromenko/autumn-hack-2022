from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from exponents.models import Exponent

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=64, write_only=True)
    emails = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = Exponent
        exclude = ['user']
        read_only_fields = ['user']
        depth = 1

    @transaction.atomic
    def create(self, validated_data):
        emails = validated_data.pop('emails')
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        user = User(emails=emails, username=username)

        user.set_password(password)
        user.save()

        return Exponent.objects.create(user=user, **validated_data)


class RegistrationConfirmationSerializer(serializers.Serializer):
    key = serializers.CharField(max_length=64)
    email = serializers.EmailField()


class LoginUsingPhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=64)


class LoginUsingPhoneConfirmationSerializer(serializers.Serializer):
    key = serializers.CharField(max_length=64)
    phone_number = serializers.CharField(max_length=64)
