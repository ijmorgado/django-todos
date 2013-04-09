from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader
from todos_app.models import Task
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
import json

def index(request):
    latest_todos = Task.objects.order_by('-creation_date')[:5]
    template = loader.get_template('tasks/index.html')
    context = Context({
        'latest_todos': latest_todos,
    })
    return HttpResponse(template.render(context))

def detail(request, todo_id):
	try:
            task = Task.objects.get(pk=todo_id)
    	except Task.DoesNotExist:
        	raise Http404
   	return render(request, 'tasks/detail.html', {'task': task})

def update(request, todo_id):
    try:
        task = Task.objects.get(pk=todo_id)
    except Task.DoesNotExist:
        raise Http404
    return render(request, 'tasks/update.html', {'task': task})
        
def save(request):
    p = get_object_or_404(Task, pk=request.POST['id'])
    p.task = request.POST['task']
    p.save(update_fields=['task'])
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    result = [p.id]
    return HttpResponse(json.dumps(result), content_type="application/json")

def not_found_404(request, template_name='system/not_found.html'):
    return render(request, template_name,{'request_path': request.path})

def internal_error_500(request,template_name='system/internal_error.html'):
	return render(request, template_name)