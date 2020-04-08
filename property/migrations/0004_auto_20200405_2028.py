from django.db import migrations


def set_new_bulding(apps, schema_editor):
    threshold = 2015
    Flat = apps.get_model("property", "Flat")
    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year >= threshold
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0003_flat_new_building"),
    ]

    operations = [migrations.RunPython(set_new_bulding)]
