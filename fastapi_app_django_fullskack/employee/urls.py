from django.urls import path
from . import views

app_name = 'employee'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('employee/create/', views.CreateView.as_view(), name='create'),
    path('employee/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('employee/<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('employee/<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]