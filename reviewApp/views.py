
from django.views.generic import ListView, DeleteView
from django.views.generic import dates
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.views.generic.detail import DetailView

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
   