from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app.payment.create_invoice import create_invoice
from app.treatment.models import Treatment
from utills.page_res import page_repose
from .filters import PaymentFilter
from .form import PaymentForm
from .models import Payment

def permission_for(permssion, request):
    if not request.user.is_superuser and not request.user.type == permssion :
        html_template = loader.get_template( 'page-403.html' )
        return HttpResponse(html_template.render({}, request), status=403)


@login_required(login_url="/login/")
def pay_list(request):
    permission_for('Employee', request)
    
    q = Payment.objects.select_related('treatment', 'treatment__user','treatment__patient').all()
    
    filter = PaymentFilter(request.GET, queryset=q)
    paginator = Paginator(filter.qs, 15) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = page_repose(page_obj)

    context['segment'] = 'payment'
    context['filter'] = filter

    html_template = loader.get_template( 'payment/index.html' )
    return HttpResponse(html_template.render(context, request))




@login_required(login_url="/login/")
def pay_create(request, pk):
    
    permission_for('Employee', request)
    
    try:
        treatment = Treatment.objects\
        .only('uuid','total_amount','paid_amount','user__name',"patient__name","treatment_time")\
        .select_related('user', 'patient')\
        .get(uuid = pk)
        
    except Treatment.DoesNotExist:
        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render({}, request))
    
    if request.method == "POST": 
        
        form = PaymentForm(request.POST)

        if form.is_valid(): 

            payment = form.instance
            payment.treatment = treatment
            payment.save()
            create_invoice(treatment.uuid)
            
            
            
        return redirect(f'/payment/')
    
    elif request.method == "GET":

        context = {
            'treatment':treatment.__dict__, 
            'user':treatment.user.__dict__,
            'patient':treatment.patient.__dict__,
            'money_left': treatment.total_amount - treatment.paid_amount,
            "form": PaymentForm(), 
            "segment":'completed'
        }
        html_template = loader.get_template( 'payment/detail/index.html' )
        return HttpResponse(html_template.render(context, request))

    else:
        context = {}
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

