from django.urls import path # type: ignore
from todos.views import TodoListView, TodoCreateView, TodoUpdateView


urlpatterns = [
  path('', TodoListView.as_view(), name='todo_list'),
  path('create/', TodoCreateView.as_view(), name='todo_create'),
  path('update/<int:pk>/', TodoUpdateView.as_view(), name='todo_update')]