from django.http import HttpResponse
from django.template import Context, loader
from todos_app.models import Task
from django.shortcuts import render
from django.http import Http404

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
        