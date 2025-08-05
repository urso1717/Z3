from django.shortcuts import render

# Create your views here.

from .models import Component

def component_view(request):
    data = Component.objects.all()
    return render(request, 'component.html', { 'data': data } )

### THIS FILE DOESN'T MATTER - DELETE IT ###