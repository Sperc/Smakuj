from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render, redirect
from .models import Category,Dish
from django.views.generic import CreateView, UpdateView, DetailView,View,DeleteView
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm

def index(request):
    all_category = Category.objects.all()
    context = {'all_category': all_category}
    return render(request,'przepis/index.html', context)

def detail(request,category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("Category doesn't exists")
    return render(request, "przepis/details.html", {'category': category})

def receipe(request,category_id,dish_id):
    dish = Dish.objects.get(pk=dish_id)
    category = Category.objects.get(pk=category_id)
    return render(request,"przepis/receipe.html", {'dish':dish,'category':category})


class DishCreate(CreateView):
    model = Dish
    fields = ['category','dish_logo','dish_receipe','dish_title']

class DishUpdate(CreateView):
    model = Dish
    fields = ['category','dish_logo','dish_receipe','dish_title']

class DishDelete(DeleteView):
    model = Dish
    success_url = reverse_lazy('index')


class CategoryCreate(CreateView):
    model = Category
    fields = ['category_name','category_logo']


class UserFormView(View):
    form_class = UserForm
    template_name = 'przepis/registration_form.html'

    #dispay blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            #cleanded (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return User obiject if credntials is correct
            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')

        return render(request,self.template_name,{'form':form})


