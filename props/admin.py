from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Tag, Flair, GGMLUser, Prop


class GGMLUserInline(admin.StackedInline):
    model = GGMLUser
    can_delete = False
    verbose_name = 'GGMLUser'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (GGMLUserInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
#    list_display = ('user', 'email', 'first_name', 'last_name', 'flair', 'win_count', 'loss_count')


class PropAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_creator', 'get_takers', 'date_added', 'resolution_date', 'get_tags')

admin.site.unregister(User)

admin.site.register(Tag)
admin.site.register(Flair)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Prop, PropAdmin)
