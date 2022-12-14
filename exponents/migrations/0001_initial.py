# Generated by Django 4.1.2 on 2022-10-23 00:40

from django.conf import settings
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('emails', models.CharField(max_length=255, verbose_name="Email'ы")),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.CharField(choices=[('true', 'Опубликовано'), ('false', 'Не опубликовано'), ('rejected', 'Отклонено')], max_length=128, verbose_name='Опубликовано')),
                ('rejected_comment', models.TextField(blank=True, verbose_name='Комментарий к отклонению')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('partner_link', models.URLField()),
                ('content_type', models.CharField(choices=[('html', 'HTML'), ('video', 'Видео')], max_length=8, verbose_name='Тип контента')),
                ('html', models.TextField(blank=True)),
                ('video_link', models.URLField(blank=True)),
                ('import_substitution_shield', models.BooleanField(verbose_name='Шилд импортозамещения')),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
            },
        ),
        migrations.CreateModel(
            name='Exponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('meta_keywords', models.CharField(max_length=255)),
                ('meta_description', models.CharField(max_length=255)),
                ('about', models.TextField(verbose_name='О компании')),
                ('logo', models.ImageField(upload_to='', verbose_name='Логотип')),
                ('site_url', models.URLField(verbose_name='Адрес сайта предприятия')),
                ('notifications_email', models.EmailField(max_length=254, verbose_name='Email для уведомлений от портала')),
                ('phone_number', models.CharField(max_length=64, unique=True, verbose_name='Номер телефона')),
                ('full_contact_name', models.CharField(max_length=255, verbose_name='ФИО контактного лица')),
                ('inn', models.CharField(max_length=128, verbose_name='ИНН предприятия')),
                ('legal_address', models.CharField(max_length=255, verbose_name='Юридический адрес')),
                ('production_address', models.CharField(max_length=255, verbose_name='Адрес производства')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Экспонент',
                'verbose_name_plural': 'Экспоненты',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.CharField(choices=[('true', 'Опубликовано'), ('false', 'Не опубликовано'), ('rejected', 'Отклонено')], max_length=128, verbose_name='Опубликовано')),
                ('rejected_comment', models.TextField(blank=True, verbose_name='Комментарий к отклонению')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('text', models.TextField(verbose_name='Текст')),
                ('rate', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('full_contact_name', models.CharField(max_length=255, verbose_name='ФИО автора')),
                ('logo', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
                ('exponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exponents.exponent', verbose_name='Экспонент')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.CharField(choices=[('true', 'Опубликовано'), ('false', 'Не опубликовано'), ('rejected', 'Отклонено')], max_length=128, verbose_name='Опубликовано')),
                ('rejected_comment', models.TextField(blank=True, verbose_name='Комментарий к отклонению')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exponents.productcategory', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория продуктов',
                'verbose_name_plural': 'Категории продуктов',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.CharField(choices=[('true', 'Опубликовано'), ('false', 'Не опубликовано'), ('rejected', 'Отклонено')], max_length=128, verbose_name='Опубликовано')),
                ('rejected_comment', models.TextField(blank=True, verbose_name='Комментарий к отклонению')),
                ('type', models.CharField(choices=[('product', 'Товар'), ('service', 'Услуга')], max_length=16, verbose_name='Тип')),
                ('vendor', models.CharField(max_length=128, verbose_name='Производитель')),
                ('brand', models.CharField(max_length=128, verbose_name='Торговая марка/Бренд')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Описание')),
                ('meta_keywords', models.CharField(max_length=255)),
                ('meta_description', models.CharField(max_length=255)),
                ('purchase_type', models.CharField(choices=[('wholesale', 'Опт'), ('retail', 'Розница'), ('both', 'Опт/Розница')], max_length=16, verbose_name='Тип')),
                ('minimum_batch', models.PositiveIntegerField(verbose_name='Минимальная партия')),
                ('payment_type', models.CharField(choices=[('CASH', 'Наличная'), ('NON_CASH', 'Безналичная'), ('CARD', 'Картой'), ('ONLINE', 'Онлайн')], max_length=16, verbose_name='Способ оплаты')),
                ('delivery_type', models.CharField(choices=[('pickup', 'Самовывоз'), ('delivery', 'Доставка')], max_length=16, verbose_name='Способ доставки')),
                ('standards_following', models.BooleanField(verbose_name='Соответствие стандартам')),
                ('analogs', models.TextField(verbose_name='Аналоги')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('import_substitution_shield', models.BooleanField(verbose_name='Шильд импортозамещения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exponents.productcategory', verbose_name='Категория')),
                ('exponent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exponents.exponent', verbose_name='Экспонент')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('lat', models.TextField(verbose_name='Широта')),
                ('long', models.TextField(verbose_name='Долгота')),
                ('cooperation_type', models.TextField(verbose_name='Тип сотрудничества')),
                ('partner_site_url', models.URLField(verbose_name='Адрес сайта партнера')),
                ('active', models.BooleanField(verbose_name='Отображен на карте')),
                ('exponent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exponents.exponent', verbose_name='Экспонент')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
            },
        ),
        migrations.CreateModel(
            name='ExponentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.CharField(choices=[('true', 'Опубликовано'), ('false', 'Не опубликовано'), ('rejected', 'Отклонено')], max_length=128, verbose_name='Опубликовано')),
                ('rejected_comment', models.TextField(blank=True, verbose_name='Комментарий к отклонению')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exponents.exponentcategory', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория экспонента',
                'verbose_name_plural': 'Категории экспонентов',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('logo', models.ImageField(upload_to='', verbose_name='Логотип')),
                ('index', models.IntegerField(verbose_name='Порядок отображения')),
                ('exponent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exponents.exponent', verbose_name='Экспонент')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
                'unique_together': {('index',)},
            },
        ),
    ]
