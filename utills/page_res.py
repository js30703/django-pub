
def page_repose(page_obj):
    context ={}

    if page_obj.__dict__['number'] == 1 :
        context['pre_page'] = None
    else:
        context['pre_page'] = page_obj.__dict__['number']-1


    
    if page_obj.__dict__['number'] == page_obj.__dict__['paginator'].__dict__['num_pages'] :
        
        context['next_page'] = None
    else :
        context['next_page'] = page_obj.__dict__['number']+1

    context['object_list'] = page_obj.__dict__['object_list']
    context['current_page'] = int(page_obj.__dict__['number'])
    context['total_page'] = range(1,(page_obj.__dict__['paginator'].__dict__['num_pages']+1))
    context['count'] = page_obj.__dict__['paginator'].__dict__['count']
    return context
