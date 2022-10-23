from django.conf import settings
from django.contrib import admin, messages
from django.core.mail import send_mail
from django.db import transaction
from django.utils.translation import ngettext, gettext_lazy as _


class PublishActionsAdminMixin(admin.ModelAdmin):
    actions = ['make_published']

    @admin.action(description=_('Опубликовать выделенные записи'))
    @transaction.atomic
    def make_published(self, request, queryset):
        updated = queryset.update(is_published=True)

        model_name = queryset.model._meta.verbose_name
        model_name_plural = queryset.model._meta.verbose_name_plural

        emails_and_values = queryset.values_list('exponent__notifications_email', 'name')
        for (email, value) in emails_and_values:
            send_mail(
                subject=f'Следующие {model_name_plural} были опубликованы',
                message=f'{model_name} "{value}" был(а) опубликован(а).',
                recipient_list=[email],
                from_email=[settings.DEFAULT_FROM_EMAIL],
            )

        self.message_user(request, ngettext(
            '%d запись была опубликована.',
            '%d записей было опубликовано.',
            updated,
        ) % updated, messages.SUCCESS)
