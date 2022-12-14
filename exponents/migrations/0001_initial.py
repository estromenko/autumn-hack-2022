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
                ('emails', models.CharField(max_length=255, verbose_name="Email'??")),
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
                ('is_published', models.CharField(choices=[('true', '????????????????????????'), ('false', '???? ????????????????????????'), ('rejected', '??????????????????')], max_length=128, verbose_name='????????????????????????')),
                ('rejected_comment', models.TextField(blank=True, verbose_name='?????????????????????? ?? ????????????????????')),
                ('name', models.CharField(max_length=64, verbose_name='????????????????')),
                ('partner_link', models.URLField()),
                ('content_type', models.CharField(choices=[('html', 'HTML'), ('video', '??????????')], max_length=8, verbose_name='?????? ????????????????')),
                ('html', models.TextField(blank=True)),
                ('video_link', models.URLField(blank=True)),
                ('import_substitution_shield', models.BooleanField(verbose_name='???????? ????????????????????????????????')),
            ],
            options={
                'verbose_name': '????????',
                'verbose_name_plural': '??????????',
            },
        ),
        migrations.CreateModel(
            name='Exponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='??????')),
                ('description', models.TextField(verbose_name='????????????????')),
                ('title', models.CharField(max_length=128, verbose_name='??????????????????')),
                ('meta_keywords', models.CharField(max_length=255)),
                ('meta_description', models.CharField(max_length=255)),
                ('about', models.TextField(verbose_name='?? ????????????????')),
                ('logo', models.ImageField(upload_to='', verbose_name='??????????????')),
                ('site_url', models.URLField(verbose_name='?????????? ?????????? ??????????????????????')),
                ('notifications_email', models.EmailField(max_length=254, verbose_name='Email ?????? ?????????????????????? ???? ??????????????')),
                ('phone_number', models.CharField(max_length=64, unique=True, verbose_name='?????????? ????????????????')),
                ('full_contact_name', models.CharField(max_length=255, verbose_name='?????? ?????????????????????? ????????')),
                ('inn', models.CharField(max_length=128, verbose_name='?????? ??????????????????????')),
                ('legal_address', models.CharField(max_length=255, verbose_name='?????????????????????? ??????????')),
                ('production_address', models.CharField(max_length=255, verbose_name='?????????? ????????????????????????')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='????????????????????????')),
            ],
            options={
                'verbose_name': '??????????????????',
                'verbose_name_plural': '????????????????????',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.CharField(choices=[('true', '????????????????????????'), ('false', '???? ????????????????????????'), ('rejected', '??????????????????')], max_length=128, verbose_name='????????????????????????')),
                ('rejected_comment', models.TextField(blank=True, verbose_name='?????????????????????? ?? ????????????????????')),
                ('name', models.CharField(max_length=255, verbose_name='??????')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='???????? ????????????????????')),
                ('text', models.TextField(verbose_name='??????????')),
                ('rate', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='????????????')),
                ('full_contact_name', models.CharField(max_length=255, verbose_name='?????? ????????????')),
                ('logo', models.ImageField(blank=True, upload_to='', verbose_name='??????????????????????')),
                ('exponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exponents.exponent', verbose_name='??????????????????')),
            ],
            options={
                'verbose_name': '??????????',
                'verbose_name_plural': '????????????',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.CharField(choices=[('true', '????????????????????????'), ('false', '???? ????????????????????????'), ('rejected', '??????????????????')], max_length=128, verbose_name='????????????????????????')),
                ('rejected_comment', models.TextField(blank=True, verbose_name='?????????????????????? ?? ????????????????????')),
                ('name', models.CharField(max_length=128, verbose_name='????????????????')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exponents.productcategory', verbose_name='???????????????????????? ??????????????????')),
            ],
            options={
                'verbose_name': '?????????????????? ??????????????????',
                'verbose_name_plural': '?????????????????? ??????????????????',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.CharField(choices=[('true', '????????????????????????'), ('false', '???? ????????????????????????'), ('rejected', '??????????????????')], max_length=128, verbose_name='????????????????????????')),
                ('rejected_comment', models.TextField(blank=True, verbose_name='?????????????????????? ?? ????????????????????')),
                ('type', models.CharField(choices=[('product', '??????????'), ('service', '????????????')], max_length=16, verbose_name='??????')),
                ('vendor', models.CharField(max_length=128, verbose_name='??????????????????????????')),
                ('brand', models.CharField(max_length=128, verbose_name='???????????????? ??????????/??????????')),
                ('name', models.CharField(max_length=128, verbose_name='????????????????')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='??????????????????????')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('description', models.TextField(verbose_name='????????????????')),
                ('price', models.FloatField(verbose_name='????????????????')),
                ('meta_keywords', models.CharField(max_length=255)),
                ('meta_description', models.CharField(max_length=255)),
                ('purchase_type', models.CharField(choices=[('wholesale', '??????'), ('retail', '??????????????'), ('both', '??????/??????????????')], max_length=16, verbose_name='??????')),
                ('minimum_batch', models.PositiveIntegerField(verbose_name='?????????????????????? ????????????')),
                ('payment_type', models.CharField(choices=[('CASH', '????????????????'), ('NON_CASH', '??????????????????????'), ('CARD', '????????????'), ('ONLINE', '????????????')], max_length=16, verbose_name='???????????? ????????????')),
                ('delivery_type', models.CharField(choices=[('pickup', '??????????????????'), ('delivery', '????????????????')], max_length=16, verbose_name='???????????? ????????????????')),
                ('standards_following', models.BooleanField(verbose_name='???????????????????????? ????????????????????')),
                ('analogs', models.TextField(verbose_name='??????????????')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='???????? ????????????????????')),
                ('import_substitution_shield', models.BooleanField(verbose_name='?????????? ????????????????????????????????')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exponents.productcategory', verbose_name='??????????????????')),
                ('exponent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exponents.exponent', verbose_name='??????????????????')),
            ],
            options={
                'verbose_name': '??????????????',
                'verbose_name_plural': '????????????????',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='??????????')),
                ('name', models.CharField(max_length=255, verbose_name='??????')),
                ('lat', models.TextField(verbose_name='????????????')),
                ('long', models.TextField(verbose_name='??????????????')),
                ('cooperation_type', models.TextField(verbose_name='?????? ????????????????????????????')),
                ('partner_site_url', models.URLField(verbose_name='?????????? ?????????? ????????????????')),
                ('active', models.BooleanField(verbose_name='?????????????????? ???? ??????????')),
                ('exponent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exponents.exponent', verbose_name='??????????????????')),
            ],
            options={
                'verbose_name': '??????????????',
                'verbose_name_plural': '??????????????',
            },
        ),
        migrations.CreateModel(
            name='ExponentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.CharField(choices=[('true', '????????????????????????'), ('false', '???? ????????????????????????'), ('rejected', '??????????????????')], max_length=128, verbose_name='????????????????????????')),
                ('rejected_comment', models.TextField(blank=True, verbose_name='?????????????????????? ?? ????????????????????')),
                ('name', models.CharField(max_length=64, verbose_name='????????????????')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='???????? ????????????????????')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exponents.exponentcategory', verbose_name='???????????????????????? ??????????????????')),
            ],
            options={
                'verbose_name': '?????????????????? ????????????????????',
                'verbose_name_plural': '?????????????????? ??????????????????????',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='??????')),
                ('logo', models.ImageField(upload_to='', verbose_name='??????????????')),
                ('index', models.IntegerField(verbose_name='?????????????? ??????????????????????')),
                ('exponent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exponents.exponent', verbose_name='??????????????????')),
            ],
            options={
                'verbose_name': '??????????????',
                'verbose_name_plural': '????????????????',
                'unique_together': {('index',)},
            },
        ),
    ]
