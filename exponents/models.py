from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from exponents.managers import UserManager


class User(AbstractUser):
    email = None
    emails = models.CharField(_("Email'ы"), max_length=255)

    REQUIRED_FIELDS = ['emails']

    objects = UserManager()


class Exponent(models.Model):
    user = models.OneToOneField(User, verbose_name=_('Пользователь'), on_delete=models.CASCADE)
    name = models.CharField(_('Имя'), max_length=255)
    description = models.TextField(_('Описание'))
    title = models.CharField(_('Заголовок'), max_length=128)
    meta_keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    about = models.TextField(_('О компании'))
    logo = models.ImageField(_('Логотип'))
    category = None
    site_url = models.URLField(_('Адрес сайта предприятия'))
    notifications_email = models.EmailField(_('Email для уведомлений от портала'))
    phone_number = models.CharField(_('Номер телефона'), max_length=64, unique=True)
    full_contact_name = models.CharField(_('ФИО контактного лица'), max_length=255)
    inn = models.CharField(_('ИНН предприятия'), max_length=128)
    legal_address = models.CharField(_('Юридический адрес'), max_length=255)
    production_address = models.CharField(_('Адрес производства'), max_length=255)
    locations_table = None
    partners = None
    partners_reviews = None

    objects = models.Manager()

    class Meta:
        verbose_name = _('Экспонент')
        verbose_name_plural = _('Экспоненты')
