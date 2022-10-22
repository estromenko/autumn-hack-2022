from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.db import transaction
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from sms import send_sms

from authentication.serializers import (
    RegistrationSerializer,
    LoginUsingPhoneSerializer,
    RegistrationConfirmationSerializer,
    LoginUsingPhoneConfirmationSerializer,
)
from authentication.mixins import KeyGeneratorMixin
from exponents.models import Exponent


REGISTRATION_CACHE_PREFIX = 'registration_confirmation_'
LOGIN_CACHE_PREFIX = 'login_confirmation_'
CACHE_TTL = 3 * 60


class RegistrationAPIView(generics.CreateAPIView, KeyGeneratorMixin):
    serializer_class = RegistrationSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        exponent = serializer.instance
        key = self.generate_key()

        cache.set(REGISTRATION_CACHE_PREFIX + key, exponent.notifications_email, CACHE_TTL)

        send_mail(
            subject='Код подтверждения учетной записи',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[exponent.notifications_email],
            message=f'Ваш код подтверждения: {key}'
        )

        response = {'success': 'Код подтверждения отправлен на почту'}
        return Response(response, status=status.HTTP_201_CREATED)


class RegistrationConfirmationAPIView(generics.CreateAPIView):
    serializer_class = RegistrationConfirmationSerializer
    cache_prefix = REGISTRATION_CACHE_PREFIX

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        value = cache.get(self.cache_prefix + data['key'])
        if not value or data['email'] != value:
            response = {'error': 'Введен неправильный код подтверждения'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            exponent = Exponent.objects.get(notifications_email=data['email'])
        except (Exponent.DoesNotExist, Exponent.MultipleObjectsReturned):  # type: ignore
            response = {'error': 'Некорректный пользователь'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(exponent.user)

        response = {'refresh': str(refresh), 'access': str(refresh.access_token)}
        return Response(response, status=status.HTTP_200_OK)


class LoginUsingPhoneAPIView(generics.CreateAPIView, KeyGeneratorMixin):
    serializer_class = LoginUsingPhoneSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        exponent = Exponent.objects.filter(phone_number=data['phone_number']).first()
        if not exponent or not exponent.user.check_password(data['password']):
            response = {'error': 'Некорректные данные'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        key = self.generate_key()

        cache.set(LOGIN_CACHE_PREFIX + key, data['phone_number'], CACHE_TTL)

        send_sms(
            f'Ваш код доступа для подтверждения регистрации: {key}',
            settings.SMS_PHONE_NUMBER_FROM,
            [data['phone_number']]
        )

        response = {'success': 'Код подтверждения отправлен на указанный номер телефона'}
        return Response(response, status=status.HTTP_201_CREATED)


class LoginUsingPhoneConfirmationAPIView(RegistrationConfirmationAPIView):
    serializer_class = LoginUsingPhoneConfirmationSerializer
    cache_prefix = LOGIN_CACHE_PREFIX

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        value = cache.get(self.cache_prefix + data['key'])
        if not value or data['phone_number'] != value:
            response = {'error': 'Введен неправильный код подтверждения'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            exponent = Exponent.objects.get(phone_number=data['phone_number'])
        except (Exponent.DoesNotExist, Exponent.MultipleObjectsReturned):  # type: ignore
            response = {'error': 'Некорректный пользователь'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(exponent.user)

        response = {'refresh': str(refresh), 'access': str(refresh.access_token)}
        return Response(response, status=status.HTTP_200_OK)
