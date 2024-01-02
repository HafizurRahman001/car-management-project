from django.shortcuts import render,redirect
from django.contrib import messages
from car_model.models import CarModel
from view_details.models import Purchase
from view_details.forms import PurchaseForm
from view_details.forms import CommentForm
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required(login_url='/authentication/login/'), name='dispatch')
class DetailPostView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'show_details.html'


    def post(self,request, *args, **kwargs):
        comment_form = CommentForm(self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context



@login_required(login_url='/authentication/login/')
def purchase_history(request, id):
    product = CarModel.objects.get(pk=id)
    
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            product.car_quantity = product.car_quantity - 1
            messages.success(request, f"You Purchased <span style='color: blue; font-weight:bold;'>{product.car_title}</span> Successfully")
            product.save()
            data = Purchase(author=request.user, product=product)
            data.save()
            return redirect('profile')
    else:
        form = PurchaseForm()
    return render(request, 'purchase_form.html', {'product': product, 'form': form})



