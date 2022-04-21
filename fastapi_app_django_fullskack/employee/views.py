from django.urls import reverse_lazy
from django.views import generic
from .models import TEmployee

class IndexView(generic.ListView):
    model = TEmployee
    paginate_by = 10
    template_name = 'employee/index.html'

class DetailView(generic.DetailView):
    model = TEmployee
    fields = '__all__'  # or ['colmunname', 'colmunname', 'colmunname']
    template_name = 'employee/detail.html'

class CreateView(generic.edit.CreateView):
    model = TEmployee
    fields = '__all__'  # or ['colmunname', 'colmunname', 'colmunname']
    template_name = 'employee/create.html'

class UpdateView(generic.edit.UpdateView):
    model = TEmployee
    fields = '__all__'  # or ['colmunname', 'colmunname', 'colmunname']
    template_name = 'employee/update.html'

class DeleteView(generic.edit.DeleteView):
    model = TEmployee
    success_url = reverse_lazy('employee:index')
    template_name = 'employee/delete.html'