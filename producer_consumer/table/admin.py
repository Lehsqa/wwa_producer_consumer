from django.contrib import admin
from table.models import Order, Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'


class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline, )


class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'employee')
    search_fields = ('name',)


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Order, TableAdmin)
