from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import AccessMixin


# Create your views here.
def mainPage(request):
    return render(request,'Home.html')

#--- User Creation 
class UserCreateView(CreateView):
    template_name='registration/register.html'
    form_class= UserCreationForm
    success_url = reverse_lazy('mainApp:register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

# 믹스인 클래스 추가
class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message="Owner only can update/delete object"

    def dispatch(self, request, *args, **kargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kargs)