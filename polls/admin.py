from django.contrib import admin
from .models import User, Favorite,Person


class ChoiceInLine(admin.TabularInline):
    model = Favorite
    extra = 2


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user_name']})
    ]
    inlines = [ChoiceInLine]


admin.site.register(User, UserAdmin)
admin.site.register(Person)
