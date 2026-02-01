
from .models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'discount_percentage',
        'is_active',
        'valid_from',
        'valid_until',
    )

    list_filter = (
        'is_active',
        'valid_from',
        'valid_until',
    )

    search_fields = ('code',)

    ordering = ('-valid_from',)

    readonly_fields = ()

    fieldsets = (
        ('Coupon Details', {
            'fields': ('code', 'discount_percentage')
        }),
        ('Validity', {
            'fields': ('valid_from', 'valid_until', 'is_active')
        }),
    )

