from django.contrib import admin
from exponents.models import (
    Exponent,
    Location,
    Partner,
    Product,
    ProductCategory,
    Review,
    User,
    ExponentCategory,
    Case,
)
from exponents.mixins import PublishActionsAdminMixin


@admin.register(Exponent)
class ExponentAdmin(admin.ModelAdmin):
    """Админка экспонентов. """

    list_filter = ('user__is_active', )
    list_display = ('name', 'phone_number', 'inn', 'get_active')
    search_fields = ('name', )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('user')

    def get_active(self, obj):
        return obj.user.is_active

    get_active.short_description = 'Активен'
    get_active.boolean = True


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка пользователь. """

    list_display = ('username', 'emails', 'is_active', )
    search_fields = ('username', )
    exclude = ('password', )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Админка локаций. """

    list_display = ('name', 'exponent', 'address', )
    search_fields = ('name', )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """Админка партеров. """

    list_display = ('name', 'exponent', 'index', )
    search_fields = ('name', )


@admin.register(Product)
class ProductAdmin(PublishActionsAdminMixin, admin.ModelAdmin):
    """Админка продуктов. """

    list_display = ('name', 'type', 'vendor', 'category', 'is_published', )
    search_fields = ('name', )
    exclude = ('is_published', 'rejected_comment', )


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    """Админка категории продуктов. """

    list_display = ('name', 'parent', )
    search_fields = ('name', )
    exclude = ('is_published', 'rejected_comment', )


@admin.register(Review)
class ReviewAdmin(PublishActionsAdminMixin, admin.ModelAdmin):
    """Админка отзывов. """

    list_display = ('name', 'exponent', 'is_published', )
    search_fields = ('name', )
    exclude = ('is_published', 'rejected_comment', )


@admin.register(ExponentCategory)
class ExponentCategoryAdmin(admin.ModelAdmin):
    """Админка категорий экспонента. """

    list_display = ('name', 'parent', )
    search_fields = ('name', )


@admin.register(Case)
class CaseAdmin(PublishActionsAdminMixin, admin.ModelAdmin):
    """Админка кейсов. """

    list_display = ('name', 'is_published', )
    search_fields = ('name', )
    exclude = ('is_published', 'rejected_comment', )
