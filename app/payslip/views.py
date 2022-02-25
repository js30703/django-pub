from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app.payslip.models import PaySlip


from utills.page_res import page_repose


def permission_for(permission, request):
    if permission == '':
        if request.user.is_anonymous:
            html_template = loader.get_template('page-403.html')
            return HttpResponse(html_template.render({}, request), status=403)


@login_required(login_url="/login/")
def pay_slip_list(request):
    permission_for('', request)
    q = PaySlip.objects.filter(user=request.user, status="confirmed")

    paginator = Paginator(q, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = page_repose(page_obj)
    context.update({"user": request.user})
    html_template = loader.get_template('profile.html')
    return HttpResponse(html_template.render(context, request))
