
from django.db.models import fields
from django.views.generic import ListView, DeleteView, FormView, TemplateView
from django.views.generic import dates
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.views.generic.detail import DetailView

from django.conf import settings

from django.db.models import Q
from django.shortcuts import render

from reviewApp.models import Post
from reviewApp.form import PostSearchForm

from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mainApp.views import OwnerOnlyMixin


from . models import Post


#-- ListView

class PostLV(ListView):
    model = Post
    template_name = 'review/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2
    
# DetailView                                                                               

class PostDV(DetailView):
    model = Post
    template_name = 'review/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context


#ArchiveView

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'
    template_name = 'review/post_archive.html'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list=True
    template_name = 'review/post_archive_year.html'

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = 'review/post_archive_month.html'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt' 
    template_name = 'review/post_archive_day.html'      
    
class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
   

def test(request):
    render(request, 'Review.html')
#

#--- Tag View
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context





class SearchFormView(FormView): 
    form_class = PostSearchForm 

    def form_valid(self, form): 
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) |  Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

        context = {} 
        context['form'] = form 
        context['search_term'] = searchWord
        context['object_list'] = post_list 

        return render(self.request, self.template_name, context)   # No Redirection




# add change update delete 기능

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    initial = {'slug' : 'auto-filling-do-not-input'}
    template_name = 'review/post_form.html'


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostChangeLV(LoginRequiredMixin, ListView):
    template_name= 'review/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    success_url= reverse_lazy('mainApp:main_page')
    template_name = 'review/post_form.html'

class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    template_name = "review/post_confirm_delete.html"
    success_url = reverse_lazy('mainApp:main_page')