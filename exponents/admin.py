from django.contrib import admin
from exponents.models import (
    Exponent,
    User,
)


@admin.register(Exponent)
class ExponentAdmin(admin.ModelAdmin):
    """Админка экспонентов. """


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка пользователь. """
