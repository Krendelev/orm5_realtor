import phonenumbers as phn

from django.db import migrations
from phonenumbers.phonenumberutil import NumberParseException


def normalize_phone_num(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    for flat in Flat.objects.all():
        flat.owner_phone_pure = None
        try:
            parsed = phn.parse(flat.owners_phonenumber, "RU")
        except NumberParseException:
            flat.save()
            continue
        if phn.is_valid_number(parsed):
            flat.owner_phone_pure = phn.format_number(
                parsed, phn.PhoneNumberFormat.E164
            )
        flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    for flat in Flat.objects.all():
        flat.owner_phone_pure = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0007_flat_owner_phone_pure"),
    ]

    operations = [migrations.RunPython(normalize_phone_num, move_backward)]
