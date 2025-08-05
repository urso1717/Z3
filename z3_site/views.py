from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView
from z3_app.models import Component
from z3_app.models import Bom
from z3_app.models import BomComponent
from z3_app.models import CadReference

from django.db.models import Q

def component_view(request):
    data = Component.objects.all()
    return render(request, 'component.html', { 'data': data } )

def component_search_view(request):
    # data = Component.objects.all()
    data = Component.objects.filter(component_description__icontains='Generic')
    return render(request, 'component-search.html', { 'data': data } )

class SearchResultsView(ListView):
    model = Component
    template_name = 'component-search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query == None:
            query = "" # filter doesn't like 'None' as a parameter
        object_list = Component.objects.filter(
            Q(component_description__icontains=query)
        )
        return object_list
    # get_queryset

# SearchResultsView

def get_cad_references( bom_component_id ):

    cad_refs = CadReference.objects.filter( bom_component_id = bom_component_id ).values()
    return cad_refs

# get_cad_references

def get_bom_components( bom_id ):
    return BomComponent.objects.filter( bom_id = bom_id )

# get_bom_components

def get_component_name_and_description( component_id ):
    name = "Component name not found for component_id " + str( component_id )
    desc = "Description not found"
    try:
        name = Component.objects.get( component_id = component_id )
    except Exception:
        print( "==== component name not found for component id " + str( component_id ))

    return name

# get_component_name

def tree_view(request):
    boms = Bom.objects.all() # temporary
    # For each bom, get its bom_components
    for bom in boms:
        # get the children and add them to each bom (TODO)
        bom_components = get_bom_components( bom.bom_id )
        print( "==== bom_components: " + str( bom_components ) )
        for bc in bom_components:
            bom.component_id = bc.bom_component_id
            bom.component_name = get_component_name_and_description( bc.component_id )
            bom.component_description = bom.component_name.component_description
            bom.component    = bc.component
            bom.cad_reference = get_cad_references( bc.bom_component_id )
        # for
    # for
    data = Component.objects.all() # temporary
    return render(request, 'tree-view.html', { 'data': data, 'boms': boms } )