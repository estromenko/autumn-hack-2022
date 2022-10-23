from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from exponents.managers import UserManager


class PublishedMixin(models.Model):
    PUBLISHED_TYPES = [
        ('true', _('Опубликовано'),),
        ('false', _('Не опубликовано'),),
        ('rejected', _('Отклонено'),),
    ]

    is_published = models.CharField(_('Опубликовано'), choices=PUBLISHED_TYPES, max_length=128)
    rejected_comment = models.TextField(_('Комментарий к отклонению'), blank=True)

    class Meta:
        abstract = True


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
    site_url = models.URLField(_('Адрес сайта предприятия'))
    notifications_email = models.EmailField(_('Email для уведомлений от портала'))
    phone_number = models.CharField(_('Номер телефона'), max_length=64, unique=True)
    full_contact_name = models.CharField(_('ФИО контактного лица'), max_length=255)
    inn = models.CharField(_('ИНН предприятия'), max_length=128)
    legal_address = models.CharField(_('Юридический адрес'), max_length=255)
    production_address = models.CharField(_('Адрес производства'), max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Экспонент')
        verbose_name_plural = _('Экспоненты')


class Location(models.Model):
    address = models.TextField(_('Адрес'))
    name = models.CharField(_('Имя'), max_length=255)
    lat = models.TextField(_('Широта'))
    long = models.TextField(_('Долгота'))
    cooperation_type = models.TextField(_('Тип сотрудничества'))
    partner_site_url = models.URLField(_('Адрес сайта партнера'))
    active = models.BooleanField(_('Отображен на карте'))
    exponent = models.ForeignKey(Exponent, verbose_name=_('Экспонент'), on_delete=models.SET_NULL,
                                 null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Локация')
        verbose_name_plural = _('Локации')


class Partner(models.Model):
    name = models.CharField(_('Имя'), max_length=255)
    logo = models.ImageField(_('Логотип'))
    index = models.IntegerField(_('Порядок отображения'))
    exponent = models.ForeignKey(Exponent, verbose_name=_('Экспонент'), on_delete=models.SET_NULL,
                                 null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('index', )
        verbose_name = _('Партнер')
        verbose_name_plural = _('Партнеры')


class ProductCategory(PublishedMixin, models.Model):
    name = models.CharField(_('Название'), max_length=128)
    parent = models.ForeignKey('self', verbose_name=_('Родительская категория'),
                               on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Категория продуктов')
        verbose_name_plural = _('Категории продуктов')


class Product(PublishedMixin, models.Model):
    PRODUCT_TYPES = (
        ('product', _('Товар')),
        ('service', _('Услуга')),
    )
    PURCHASE_TYPES = (
        ('wholesale', _('Опт')),
        ('retail', _('Розница')),
        ('both', _('Опт/Розница')),
    )
    PAYMENT_TYPES = (
        ('CASH', _('Наличная')),
        ('NON_CASH', _('Безналичная')),
        ('CARD', _('Картой')),
        ('ONLINE', _('Онлайн')),
    )
    DELIVERY_TYPES = (
        ('pickup', _('Самовывоз')),
        ('delivery', _('Доставка')),
    )

    type = models.CharField(_('Тип'), choices=PRODUCT_TYPES, max_length=16)
    vendor = models.CharField(_('Производитель'), max_length=128)
    brand = models.CharField(_('Торговая марка/Бренд'), max_length=128)
    name = models.CharField(_('Название'), max_length=128)
    image = models.ImageField(_('Изображение'), blank=True)
    video = models.FileField(
        upload_to='videos_uploaded',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['MOV','avi','mp4','webm','mkv']),
        ]
    )
    description = models.TextField(_('Описание'))
    price = models.FloatField(_('Описание'))
    meta_keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    exponent = models.ForeignKey(Exponent, verbose_name=_('Экспонент'), on_delete=models.SET_NULL,
                                 null=True, blank=True)
    category = models.ForeignKey(ProductCategory, verbose_name=_('Категория'),
                                 on_delete=models.SET_NULL, null=True, blank=True)
    purchase_type = models.CharField(_('Тип'), choices=PURCHASE_TYPES, max_length=16)
    minimum_batch = models.PositiveIntegerField(_('Минимальная партия'))
    payment_type = models.CharField(_('Способ оплаты'), choices=PAYMENT_TYPES, max_length=16)
    delivery_type = models.CharField(_('Способ доставки'), choices=DELIVERY_TYPES, max_length=16)
    standards_following = models.BooleanField(_('Соответствие стандартам'))
    analogs = models.TextField(_('Аналоги'))
    created_at = models.DateTimeField(_('Дата публикации'), auto_now_add=True)
    import_substitution_shield = models.BooleanField(_('Шильд импортозамещения'))

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


class Review(PublishedMixin, models.Model):
    name = models.CharField(_('Имя'), max_length=255)
    created_at = models.DateTimeField(_('Дата публикации'), auto_now_add=True)
    text = models.TextField(_('Текст'))
    rate = models.PositiveIntegerField(_('Оценка'), validators=[MaxValueValidator(5)])
    full_contact_name = models.CharField(_('ФИО автора'), max_length=255)
    logo = models.ImageField(_('Изображение'), blank=True)
    exponent = models.ForeignKey(Exponent, verbose_name=_('Экспонент'), on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')


class ExponentCategory(PublishedMixin, models.Model):
    name = models.CharField(_('Название'), max_length=64)
    parent = models.ForeignKey('self', verbose_name=_('Родительская категория'),
                               on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(_('Дата публикации'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Категория экспонента')
        verbose_name_plural = _('Категории экспонентов')


class Case(PublishedMixin, models.Model):
    CONTENT_TYPES = [
        ('html', _('HTML'),),
        ('video', _('Видео'),),
    ]

    name = models.CharField(_('Название'), max_length=64)
    partner_link = models.URLField()
    content_type = models.CharField(_('Тип контента'), choices=CONTENT_TYPES, max_length=8)
    html = models.TextField(blank=True)
    video_link = models.URLField(blank=True)
    import_substitution_shield = models.BooleanField(_('Шилд импортозамещения'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Кейс')
        verbose_name_plural = _('Кейсы')
