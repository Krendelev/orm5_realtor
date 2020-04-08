from django.db import migrations


def set_owner(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Owner = apps.get_model("property", "Owner")
    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            phone_pure=flat.owner_phone_pure,
        )
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0009_owner"),
    ]

    operations = [migrations.RunPython(set_owner)]
