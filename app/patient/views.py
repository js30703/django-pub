# -*- encoding: utf-8 -

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse
from django.db.models import F, query
from django import template
from .forms import PatientForm, OdontogramForm
from .models import Patient, Odontogram
from .filters import PatientFilter
from utills.page_res import page_repose

@login_required(login_url="/login/")

def list(request):
    query =  PatientFilter(request.GET, queryset=Patient.objects.filter(branch= request.user.branch))
    paginator = Paginator(query.qs.all(), 15)     
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = page_repose(page_obj)
    context['segment'] = 'patient'
    context['filter'] = query
    html_template = loader.get_template( 'patient/list.html' )
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def create(request):
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            
            form.save()
            form.instance.odontogram = Odontogram.objects.create()
            form.instance.branch = request.user.branch
            form.instance.save()
            
            return redirect('patient_list')

    context = {'form':form}
    context['segment'] = 'patient'
    
    html_template = loader.get_template( 'patient/create.html' )
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def detail(request, pk):
    
    instance = Patient.objects.select_related('odontogram').get(uuid=pk)
    
    if request.method == "POST":

        if 'name' in request.POST:
            form = PatientForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                
                return redirect('patient_list')
        elif 't_11_1' in request.POST:
            form = OdontogramForm(request.POST or None, instance=instance.odontogram)
            if form.is_valid():
                form.save()
                
                return redirect('patient_list')
    elif request.method == "GET":
        form = PatientForm(instance=instance)
        
        od_form = OdontogramForm(instance = instance.odontogram)
        context = {'form':form, 'od_form':od_form}
        
        context['segment'] = 'patient'
        html_template = loader.get_template( 'patient/update.html' )
        return HttpResponse(html_template.render(context, request))
    else:
        context ={}
        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))      
