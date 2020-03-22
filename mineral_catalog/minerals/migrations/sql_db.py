from django.db import migrations, transaction
from django.db.utils import IntegrityError

import json

@transaction.atomic
def sql_db(apps, schema_editor):
    '''Gets data from json file into database'''
    mineral_model = apps.get_model('minerals', 'Mineral')
    with open('json/minerals.json') as mineralfile:
        minerals = json.load(mineralfile)
        for mineral in minerals:
            with transaction.atomic():
                try:
                    mineral_model.objects.create(
                        name=mineral.get('name', ''),
                        image_filename=mineral.get('image_filename', ''),
                        image_caption=mineral.get('image_caption', ''),
                        category=mineral.get('category', ''),
                        formula=mineral.get('formula', ''),
                        strunz_classification=mineral.get('strunz_classification', ''),
                        color=mineral.get('color', ''),
                        crystal_system=mineral.get('crystal_system', ''),
                        unit_cell=mineral.get('unit_cell', ''),
                        crystal_symmetry=mineral.get('crystal_symmetry', ''),
                        cleavage=mineral.get('cleavage', ''),
                        mohs_scale_hardness=mineral.get('mohs_scale_hardness', ''),
                        luster=mineral.get('luster', ''),
                        streak=mineral.get('streak', ''),
                        diaphaneity=mineral.get('diaphaneity', ''),
                        optical_properties=mineral.get('optical_properties', ''),
                        refractive_index=mineral.get('refractive_index', ''),
                        crystal_habit=mineral.get('crystal_habit', ''),
                        specific_gravity=mineral.get('specific_gravity', ''),
                        group=mineral.get('group', '')
                    )
                except IntegrityError:
                    continue

class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(sql_db)
    ]