from django.contrib import admin

from .models import Complaint, Flat, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "flat_owners")
    readonly_fields = ("created_at",)
    list_display = (
        "address",
        "price",
        "new_building",
        "construction_year",
        "town",
        "get_owner",
    )
    list_editable = ("new_building",)
    list_filter = ("new_building", "rooms_number", "has_balcony")
    raw_id_fields = ("liked_by",)

    def get_owner(self, obj):
        return "\n".join([owner.name for owner in obj.flat_owners.all()])

    get_owner.short_description = "Владелец"


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("author", "complaint_about")


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats_owned",)
    list_display = ("name", "get_address", "phonenumber", "phone_pure")

    def get_address(self, obj):
        return "\n".join(
            [f"{flat.town} {flat.address}" for flat in obj.flats_owned.all()]
        )

    get_address.short_description = "Адрес квартиры"


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
