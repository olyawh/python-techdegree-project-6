from django.test import TestCase
from django.urls import reverse

from .models import Mineral

class MineralModelTests(TestCase):
    '''To test if a Mineral model works correctly'''
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
             name = 'Malachites',
             image_filename = 'malachite.jpg',
             image_caption = 'Beautiful dark green malachite mineral',
             category = 'Carbonate mineral',
             formula = 'Cu2CO3(OH)2',
             strunz_classification = 'Null',
             color = '5.BA.10',
             crystal_system = 'Monoclinic',
             unit_cell = 'Null',
             crystal_symmetry = 'Null',
             cleavage = 'Perfect on 201 fair on 010',
             mohs_scale_hardness = '3.5-4',
             luster = 'Adamantine to vitrous',
             streak = 'Light green',
             diaphaneity = 'Translucent to opaque',
             optical_properties = 'Biaxial(-)',
             refractive_index = 'na=1.6555 nb=1.875 ny=1.909',
             crystal_habit = 'Massive, botryoidal',
             group = 'Null'
        )
        name = 'Malachites'
        self.assertEqual(mineral.name, name)

class MineralViewsTest(TestCase):
    '''To test if mineral view and detail view work as intended'''
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name = 'Ajoites',
            image_filename = 'Ajoite.jpg',
            image_caption = 'Ajoite from Arizona (size: 2.4\u00d72.4\u00d72.0 cm)',
            category = 'Silicate',
            formula = '(Na,K)Cu<sub>7</sub>AlSi<sub>9</sub>O<sub>24</sub>(OH)<sub>6</sub>\u00b7<sub>3</sub>(H<sub>2</sub>O)',
            strunz_classification = '09.EA.708/D.07-10',
            crystal_system = 'Triclinic',
            unit_cell = 'a = 13.63 \u00c5, b = 14.5 \u00c5, c = 13.62 \u00c5; \u03b1 = 107.16\u00b0, \u03b2 = 105.45\u00b0, \u03b3 = 110.57\u00b0',
            color = 'Bluish green',
            crystal_symmetry = 'Triclinic 1 or 1',
            cleavage = 'Perfect on {010}',
            mohs_scale_hardness = '3\u00bd',
            luster = 'Vitreous',
            streak = 'Greenish white',
            diaphaneity = 'Translucent',
            optical_properties = 'Biaxial (+)',
            refractive_index = 'n\u03b1 = 1.550, n\u03b2 = 1.583, n\u03b3 = 1.641',
            crystal_habit = 'Sprays of bladed prismatic crystals',
            specific_gravity = '2.96',
            group = 'Silicates',
        )
        self.mineral2 = Mineral.objects.create(
            name = 'Andorites',
            image_filename = 'Andorite.jpg',
            image_caption = 'Andorite - Itos Mine, Oruro City, Cercado Province, Bolivia. Specimen height is 4.1 cm.',
            category = 'Sulfosalt',
            formula = 'PbAgSb<sub>3</sub>S<sub>6</sub>',
            strunz_classification = '02.JB.40a',
            crystal_system = 'orthorhombic',
            unit_cell = 'a = 12.99 \u00c5, b = 19.14 \u00c5, c = 4.3 \u00c5; Z = 4',
            color = 'Dark steel-gray, may tarnish yellow or iridescent; white in polished section',
            crystal_symmetry = 'Orthorhombic (2/m 2/m 2/m) dipyramidal',
            cleavage = 'none observed',
            mohs_scale_hardness = '3 - 3.5',
            luster = 'metallic',
            streak = 'Black',
            diaphaneity = 'Opaque',
            optical_properties = 'anisotropic',
            crystal_habit = 'Crystals stout prismatic to tabular on {100}, striations parallel to ; massive',
            specific_gravity = '5.33 - 5.37',
            group = 'Sulfosalts',
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs= {'pk':self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])


