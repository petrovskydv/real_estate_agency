from django.contrib import admin

from .models import Claim
from .models import Flat
from .models import Owner


class OwnersInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ('owner', 'flat')


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [
        OwnersInline,
    ]


class ClaimAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat')
    raw_id_fields = ('user', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'owner_pure_phone',)
    list_display = ('owner', 'owner_pure_phone',)
    raw_id_fields = ('flat',)
    inlines = [
        OwnersInline,
    ]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
