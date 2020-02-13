from django.contrib import admin

from .models import Account, Task, AccountTask
from django.utils.translation import ugettext_lazy as _


class PerformerTaskTabularInline(admin.TabularInline):
    model = AccountTask
    fk_name = 'performer'
    verbose_name = _('Исполняющий')
    verbose_name_plural = _('Исполняющий')
    fields = ('task', )
    extra = 1


class ReviewerTaskTabularInline(admin.TabularInline):
    model = AccountTask
    fk_name = 'reviewer'
    verbose_name = _('Ответственный')
    verbose_name_plural = _('Ответственный')
    fields = ('task', 'performer', )
    extra = 1


class PerformerAccountTabularInline(admin.TabularInline):
    model = AccountTask
    fk_name = 'task'
    verbose_name = _('Работают с задачей')
    verbose_name_plural = _('Работают с задачей')
    extra = 1


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'city', 'is_admin', )
    search_fields = ('name', 'position', 'city', )
    list_filter = ('position', 'city', 'is_admin', )
    inlines = (
        PerformerTaskTabularInline,
        ReviewerTaskTabularInline,
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', )
    search_fields = ('name', 'description', )
    inlines = (PerformerAccountTabularInline, )
