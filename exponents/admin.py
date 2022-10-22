from django.contrib import admin
from exponents.models import (
    Exponent,
    User,
)


@admin.register(Exponent)
class ExponentAdmin(admin.ModelAdmin):
    """Админка экспонентов. """

    list_filter = ('user__is_active', )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('user')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка пользователь. """
