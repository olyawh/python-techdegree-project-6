from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Mineral

def mineral_list(request):
    '''View of the list of minerals. Displaying the name of each mineral'''
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})

def mineral_detail(request, pk):
    '''View of each mineral's detail information'''
    mineral = get_object_or_404(Mineral, pk=pk)
    mineral_properties = []
    prop_list = ['category', 'formula', 'strunz_classification', 'color',
                'crystal_system', 'unit_cell', 'crystal_symmetry', 'cleavage',
                'mohs_scale_hardness', 'luster', 'streak', 'diaphaneity',
                'optical_properties', 'refractive_index ', 'crystal_habit',
                'specific_gravity', 'group']
    for prop in prop_list:
        prop_char = getattr(mineral, prop, False)
        if prop_char:
            mineral_properties.append({prop: prop_char})
    context = { 'mineral': mineral, 'mineral_properties': mineral_properties,}
    return render(request, 'minerals/mineral_detail.html', context)




