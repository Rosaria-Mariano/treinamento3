from django.urls import reverse_lazy # type: ignore
from django.views.generic import ListView, CreateView, UpdateView # type: ignore
from .models import Todo

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title','deadline']
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title','deadline']
    success_url = reverse_lazy('todo_list')