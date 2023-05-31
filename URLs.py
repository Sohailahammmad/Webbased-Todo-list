from django.urls import path
from todolist.views import TodoItemCreateView, TodoItemDetailView, TodoItemListView, TodoItemUpdateView, TodoItemDeleteView

urlpatterns = [
    path('api/todo/create/', TodoItemCreateView.as_view(), name='todo-create'),
    path('api/todo/<int:pk>/', TodoItemDetailView.as_view(), name='todo-detail'),
    path('api/todo/', TodoItemListView.as_view(), name='todo-list'),
    path('api/todo/<int:pk>/update/', TodoItemUpdateView.as_view(), name='todo-update'),
    path('api/todo/<int:pk>/delete/', TodoItemDeleteView.as_view(), name='todo-delete'),
]
