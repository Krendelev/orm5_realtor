from django.db import migrations


def set_flat_owned(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Owner = apps.get_model("property", "Owner")
    for owner in Owner.objects.all():
        flats = list(Flat.objects.filter(owner__contains=owner.name))
        owner.flats_owned.set(flats)
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0010_auto_20200407_1839"),
    ]

    operations = [migrations.RunPython(set_flat_owned)]
