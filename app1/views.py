from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.conf import settings
from django.urls import reverse_lazy
# Create your views here.

class Homeview(TemplateView):
    template_name='base.html'

class CreatePostViews(LoginRequiredMixin,CreateView):
    model=WebShop
    fields=[
        'title',
        'img',
        'price',
        'text',
    ]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    template_name='create.html'


class UpdatePostViews(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=WebShop
    fields=[
        'title',
        'img',
        'price',
        'text',
    ]
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    template_name='update.html'

class DetailViews1(DeleteView):
    model=WebShop
    template_name='detail.html'
    context_object_name="WebShop"
class Deleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=WebShop
    template_name='delete.html'
    success_url = reverse_lazy('home')
    context_object_name="WebShop"
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# class TestViews(ListView):
#     model=WebShop
#     template_name='home.html'
#     context_object_name="WebShop"
#     class Meet(CreateView):
#             model=WebShop
#     template_name='home.html'
#     context_object_name="WebShop"
#     fields=[
#         'title',
#         'img',
#         'price',
#         'text',
#     ]
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
class TestViews(CreateView, ListView):
    model = WebShop
    template_name = 'home.html'
    fields=[
        'title',
        'img',
        'price',
        'text',
    ]
    context_object_name="WebShop"
    success_url = reverse_lazy('test-show')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        queryset = super().get_queryset()
        current_user = self.request.user
        queryset = queryset.filter(author=current_user)
        return queryset
    
    def my_posts(request):
        WebShop = WebShop.objects.filter(author=request.user)
        return render(request, 'home.html', {'WebShop': WebShop})
    
class PostDeleteView(DeleteView):
    model = WebShop
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('test-show')
    context_object_name="WebShop"


class PostDeleteView(DeleteView):
    model = WebShop
    template_name = 'delete.html'
    success_url = reverse_lazy('test-show')

class rel1(TemplateView):
    template_name="categores/new_users.html"