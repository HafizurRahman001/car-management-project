from django.shortcuts import render,redirect
from django.contrib import messages
from brand_model.forms import BrandModelForm
from brand_model.models import BrandModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy


# Create your views here.
# def add_brand(request):
#     if request.method == 'POST':
#         add_car_brand_form = BrandModelForm(request.POST)
#         if add_car_brand_form.is_valid():
#             add_car_brand_form.instance.author = request.user
#             add_car_brand_form.save()
#             messages.success(request,'A New Car Brand Has been Added Successfully')
#             return redirect('home')
#     else:
#         add_car_brand_form = BrandModelForm()
#     return render(request,'car_form.html', {'form':add_car_brand_form})





@method_decorator(login_required(login_url='/authentication/login/'), name='dispatch')
class AddBrand(CreateView):
    model = BrandModel
    form_class = BrandModelForm
    template_name = 'car_form.html' # J page a data gula show korabo
    success_url = reverse_lazy('home') # kaj sheshe je page a return korbo
    def form_valid(self, form):  # j data gula frontend a pass korbo form diye
        messages.success(self.request, "A New Car Brand Has been Added Successfully")
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add your text or variable to the context
        context['type'] = 'Car Brand'
        return context