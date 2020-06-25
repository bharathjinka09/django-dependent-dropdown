from django.shortcuts import render

import json

from .models import Person, get_cs_strings, get_b_strings
from .forms import PersonForm

# Create your views here.


def personform_page(request):
    context = {}
    if request.method == 'POST':
        personform = PersonForm(request.POST)
        if personform.is_valid():
            # name = request.POST['name']
            # subject = request.POST['subject']
            # job = request.POST['job']

            personform.save()
            personform = PersonForm()
            
        else:
            personform = PersonForm()
        context['personform'] = personform

    cs_strings = get_cs_strings()
    b_strings = get_b_strings()

    json_cs_strings = json.dumps(cs_strings)
    json_b_strings = json.dumps(b_strings)

    context['json_cs_strings'] = json_cs_strings
    context['json_b_strings'] = json_b_strings

    return render(request, 'app1/personform_page.html', context)
