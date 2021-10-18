from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def todoView(request):
    todo_items = TodoItem.objects.all()
    
    return render(request, 'todo.html', 
        {'all_items': todo_items})

# create new todo and save it
# redirect browser to /todo/
def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')