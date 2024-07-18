from cars.models import Car, Brand
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CarsListView(ListView):
	model = Car
	template_name = 'cars.html'
	context_object_name = 'cars'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['brands'] = Brand.objects.all().order_by('name')
		return context

	
	def get_queryset(self):
		cars = super().get_queryset().order_by('model')
		search_brand = self.request.GET.get('search_brand')
		search_model = self.request.GET.get('search_model')
		if search_brand:
			cars = cars.filter(brand__name__icontains=search_brand)
		if search_model:
			cars = cars.filter(model__icontains=search_model)
		return cars


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarCreateView(CreateView):
	model = Car
	form_class = CarModelForm
	template_name = 'car_create.html'
	success_url = '/cars/'


class CarDetailView(DetailView):
	model = Car
	template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
	model = Car
	form_class = CarModelForm
	template_name = 'car_update.html'
	success_url = '/cars/'

	def get_success_url(self):
		return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
	

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
	model = Car
	template_name = 'car_delete.html'
	success_url = '/cars/'