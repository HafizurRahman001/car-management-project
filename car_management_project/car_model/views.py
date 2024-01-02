from django.shortcuts import render,redirect
from django.contrib import messages
from car_model.forms import CarForm
from car_model.models import CarModel
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
# def add_car(request):
#     if request.method == 'POST':
#         add_car = CarForm(request.POST, request.FILES)
#         if add_car.is_valid():
#             add_car.instance.author = request.user
#             add_car.save()
#             messages.success(request,'A New Car Has been Added Successfully')
#             return redirect('display_car')
#     else:
#         add_car = CarForm()
#     return render(request,'car_form.html', {'form':add_car})




# @method_decorator(login_required, name='dispatch')
@method_decorator(login_required(login_url='/authentication/login/'), name='dispatch')
class AddCar(CreateView):
    model = CarModel
    form_class = CarForm
    template_name = 'car_form.html' # J page a data gula show korabo
    success_url = reverse_lazy('home') # kaj sheshe je page a return korbo
    # success_url = '/posts_app/add_post/'
    def form_valid(self, form):  # j data gula frontend a pass korbo form diye
        messages.success(self.request, "Added post Successfully")
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add your text or variable to the context
        context['type'] = 'Car'
        return context