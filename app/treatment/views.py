# -*- encoding: utf-8 -
import os

from django.core.files.base import ContentFile
from app.patient.models import Patient
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse
from django.db.models import Prefetch
from django.db.models import Q
from app.patient.forms import OdontogramForm
from .form import TreatmentForm, ProductForm, TreatmentUpdateForm
from .models import Treatment, Product, Service
from .filters import ServiceFilter
from utills.pdf.draw_invoice import draw_invoice
from utills.page_res import page_repose
from rest_framework_simplejwt.tokens import RefreshToken
        
@login_required(login_url="/login/")
def list(request):

    # get_queryset
    q = Treatment.objects\
        .select_related('user', 'patient')\
        .filter(branch= request.user.branch)\
        .order_by('status','-treatment_time')
        
    is_pay_page = request.GET.get('status', None)  == 'completed'
         
    if request.user.type == 'Doctor' and not is_pay_page:
        q = q.filter(user=request.user).filter(Q(status= 'Created'))
    elif request.user.type == 'Nurse' and not is_pay_page:
        q = q.filter(Q(status= 'Created') )
    elif request.user.type == 'Employee' and is_pay_page:
        q = q.filter(status= 'Treated')
    elif request.user.is_superuser:
        pass
    else:
        html_template = loader.get_template( 'page-403.html' )
        return HttpResponse(html_template.render({}, request), status = 403)
        
    
    # pagination
    paginator = Paginator(q, 15) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = page_repose(page_obj)

    context['segment'] = 'treatment'
    if is_pay_page : context['segment'] = 'completed'
    html_template = loader.get_template( 'treatment/list.html' )
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def create(request, userpk):
    
    if request.user.type == 'Employee' or request.user.is_superuser :
        form = TreatmentForm(request=request)
        if request.method == "POST":
            if Patient.objects.get(uuid=userpk): #request.user.type == "EMP" 
                form = TreatmentForm(request.POST)
                if form.is_valid():
                    form.save()
                    form.instance.patient = Patient.objects.get(uuid=userpk)
                    form.instance.branch = request.user.branch
                    form.instance.save()
                    
                    return redirect('/patient/')
        
        context = {'form':form, 'patient':Patient.objects.get(uuid=userpk)}

        context['segment'] = 'treatment'
        html_template = loader.get_template( 'treatment/create.html' )
        return HttpResponse(html_template.render(context, request))
    
    else:
        html_template = loader.get_template( 'page-403.html' )
        return HttpResponse(html_template.render({}, request), status = 403)




@login_required(login_url="/login/")
def detail(request, pk):
    
    try:
        instance = Treatment.objects\
        .select_related('user', 'patient','patient__odontogram')\
        .prefetch_related(
            Prefetch(
                'product_set', 
                queryset= Product.objects.select_related('service').all(), 
                to_attr='services'))\
        .filter(status="Created")\
        .get(uuid = pk)\
        
    except Treatment.DoesNotExist:
        context = {}
        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))
    
    if request.user == instance.user or request.user.is_superuser or request.user.type=='Supervisor':
        if request.method == "POST": 
            form = TreatmentUpdateForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                obj = form.instance
                total = 0
                for product in obj.services:
                    total += product.service.list_price
                obj.total_amount = total
                obj.status = "Treated"
                obj.save()
                return redirect(f'../')

                

        user = instance.user.__dict__
        patient = instance.patient.__dict__
        # Product.objects.filter(treatment__user=instance.patient).values_list('teeth','diagnosis','service')
        pd_set = [ {'pd':i.__dict__, 'service':i.service.name, 'price': i.service.list_price,} for i in instance.product_set.all()]
        
        form = ProductForm()
        od_form = OdontogramForm(instance= instance.patient.odontogram)
        tr_form = TreatmentUpdateForm(instance=instance)

        total = 0
        for i in pd_set:
            total += i['price'] * i['pd']['quantity']
            
        # medical_record = Product.objects.select_related('treatment').filter(treatment__patient=instance.patient).values('teeth','treatment__treatment_time')
        medical_record = ''
        

        context = {"context":{'treatment':instance.__dict__, 'user':user, 'patient':patient, 'pd_set':pd_set, 'total':total },
            
            "form":form, 
            'od_form':od_form,
            "tr_form":tr_form,
            "filter": ServiceFilter(),
            "status": instance.status,
            "medical_record":medical_record,
            "segment":'treatment'
        }

        html_template = loader.get_template( 'treatment/detail/index.html' )
        return HttpResponse(html_template.render(context, request))
    else:
        html_template = loader.get_template( 'page-403.html' )
        return HttpResponse(html_template.render({}, request), status=403)