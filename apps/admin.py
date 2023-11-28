from django.contrib import admin

from .models import Person, Group, Membership

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'group_names')
    inlines = [MembershipInline]

    def group_names(self, obj):
        return ", ".join([group.name for group in obj.group_set.all()])
    group_names.short_description = 'Groups'

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MembershipInline]

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('person', 'group', 'date_joined', 'invite_reason')

admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
