from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.shortcuts import redirect,get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from custom.models import *
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# 클래스형
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        fields_classes = {'username': UsernameField}

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = MyUserCreationForm
    success_url = reverse_lazy('register_done')

class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'

##메니저 홈
class ManagerHome(LoginRequiredMixin, TemplateView):
    template_name = 'manager/manager_home.html'

    def get_context_data(self, **kwargs):
        set = Custom.objects.all()
        ment = Comment.objects.all()
        context = super().get_context_data(**kwargs)
        context['sets'] = set
        context['ments'] = ment
        return context

##제품관리
class ManagerHardwareList(LoginRequiredMixin, ListView):
    model = Hardware
    template_name = 'manager/manager_hardware_list.html'

class ManagerHardwareNew(LoginRequiredMixin, CreateView):
    template_name = 'manager/manager_regular_form.html'
    model = Hardware
    fields = ('name','hardware_kind','option','hard_thumbnail')
    success_url = reverse_lazy('manager_hardware_list')

class ManagerHardwareUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'manager/manager_regular_form.html'
    model = Hardware
    fields = ['name', 'hardware_kind', 'option', 'hard_thumbnail']
    success_url = reverse_lazy('manager_hardware_list')

##필터관리
class ManagerCompaList(LoginRequiredMixin, ListView):
    template_name = 'manager/manager_compa_list.html'
    model = Compa

class ManagerCompaNew(LoginRequiredMixin, CreateView):
    template_name = 'manager/manager_regular_form.html'
    model = Compa
    fields = ('comp_mode','hardware')
    success_url = reverse_lazy('manager_compa_list')

class ManagerCompaEdit(LoginRequiredMixin, UpdateView):
    template_name = 'manager/manager_regular_form.html'
    model = Compa
    fields = ('comp_mode','hardware')
    success_url = reverse_lazy('manager_compa_list')

##유저
class ManagerUserList(LoginRequiredMixin, ListView):
    template_name = 'manager/manager_user_list.html'
    model = User

##통계
class ManagerStat(LoginRequiredMixin, TemplateView):
    template_name = 'manager/manager_stat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hards'] = Hardware.objects.all()
        return context

#마이 페이지
class MemberHome(LoginRequiredMixin, TemplateView):
    template_name = 'member/member_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sets'] = Custom.objects.filter(user=self.request.user)
        context['ments'] = Comment.objects.filter(author=self.request.user)
        return context

# 함수형
@login_required
def manager_hardware_remove(request, pk):
    some_hard = get_object_or_404(Hardware, pk=pk)
    some_hard.delete()
    return redirect('manager_hardware_list')
@login_required
def manager_compa_remove(request, pk):
    some_comp = get_object_or_404(Compa, pk=pk)
    some_comp.delete()
    return redirect('manager_compa_list')

#호환성 검사를 위한 정보 수집
def get_compa(request):
    hardId = request.GET['hwid']
    hardType = request.GET['hwtype']
    hard = serializers.serialize('json', [Hardware.objects.get(id=hardId, hardware_kind=hardType)])
    objectQuery = Compa.objects.filter(hardware=hardId)
    compa = serializers.serialize('json', list(objectQuery))
    data = {
        'hard':hard,
        'compa':compa
    }
    return JsonResponse(data)