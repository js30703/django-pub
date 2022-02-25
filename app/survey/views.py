from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse
from .forms import ICF001Form, IFC001_2Form, ICF002Form
from .models import ICF001

def _icf001_index(request):
    if request.method == 'POST':
        form = ICF001Form(request.POST)
        if form.is_valid():
            form.save()
            form_id = form.instance.id
            return redirect(f'p2/?form_id={form_id}')

    gq_id = request.GET.get('ga_id', None)
    form = ICF001Form(initial={'ga_id': gq_id})
    context = {"form":form}    # ga id 값을 받아서 폼에 넣은 후 돌려주자
    html_template = loader.get_template( '_icf001/index.html' )
    return HttpResponse(html_template.render(context, request))



def _icf001_p2(request):
    form = IFC001_2Form()
    form_id = request.GET.get('form_id', None)
    context = {}
    if not form_id :
        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))
    
    if request.method == 'POST':
        form = IFC001_2Form(request.POST)
        print(form.fields['q17'].__dict__)
        if form.is_valid():
            
            try:
                obj=ICF001.objects.get(id=form_id)
                
            except ICF001.DoesNotExist:
                html_template = loader.get_template( 'page-404.html' )
                return HttpResponse(html_template.render(context, request))

            form.instance.origin = obj
            form.save()
            

            return redirect('_icf001_end')

    context = {"form":form}    
    html_template = loader.get_template( '_icf001/p2/index.html' )
    return HttpResponse(html_template.render(context, request))

def _icf001_end(request):
    context = {} 
    html_template = loader.get_template( '_icf001/end/index.html' )
    return HttpResponse(html_template.render(context, request))




def _icf002_index(request):
    form = ICF002Form()
    context = {"form":form}
    if request.method == 'POST':
        form = ICF002Form(request.POST)
        if form.is_valid():
            form.save()
            
            context = {"form":form}
            html_template = loader.get_template( '_icf002/index.html' )
            return HttpResponse(html_template.render(context, request))

    
    context = {"form":form}    # ga id 값을 받아서 폼에 넣은 후 돌려주자
    html_template = loader.get_template( '_icf002/index.html' )
    return HttpResponse(html_template.render(context, request))