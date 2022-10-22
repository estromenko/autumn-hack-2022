# Generated by Django 4.1.2 on 2022-10-22 20:01

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
                ('is_published', models.CharField(choices=[('Опубликовано', 'true'), ('Не опубликован', 'false'), ('Отклонено', 'rejected')], max_length=128, verbose_name='Опубликовано')),
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
