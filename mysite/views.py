from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.shortcuts import redirect,get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from custom.models import Custom,Comment,Hardware,Compa, User
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
        set = Custom.objects.all()[:10]
        ment = Comment.objects.all()[:10]
        context = super().get_context_data(**kwargs)
        context['sets'] = set
        context['ments'] = ment
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous or request.user.is_member:
            return redirect('no_authority')
        return super(ManagerHome, self).dispatch(request, *args, **kwargs)
## 글관리
class ManagerSetList(LoginRequiredMixin, ListView):
    model = Custom
    template_name = 'manager/manager_set_list.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous or request.user.is_member:
            return redirect('no_authority')
        return super(ManagerSetList, self).dispatch(request, *args, **kwargs)

class ManagerCommentList(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'manager/manager_comment_list.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous or request.user.is_member:
            return redirect('no_authority')
        return super(ManagerCommentList, self).dispatch(request, *args, **kwargs)

##제품관리
class ManagerHardwareList(LoginRequiredMixin, ListView):
    model = Hardware
    template_name = 'manager/manager_hardware_list.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous or request.user.is_member:
            return redirect('no_authority')
        return super(ManagerHardwareList, self).dispatch(request, *args, **kwargs)

class ManagerHardwareNew(LoginRequiredMixin, CreateView):
    template_name = 'manager/manager_hw_form.html'
    model = Hardware
    fields = ('name','hardware_kind','option','hard_thumbnail')
    success_url = reverse_lazy('manager_hardware_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous or request.user.is_member:
            return redirect('no_authority')
        return super(ManagerHardwareNew, self).dispatch(request, *args, **kwargs)

class ManagerHardwareUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'manager/manager_hw_form.html'
    model = Hardware
    fields = ['name', 'hardware_kind', 'option', 'hard_thumbnail']
    success_url = reverse_lazy('manager_hardware_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous or request.user.is_member:
            return redirect('no_authority')
        return super(ManagerHardwareUpdate, self).dispatch(request, *args, **kwargs)

##필터관리
class ManagerCompaList(LoginRequiredMixin, ListView):
    template_name = 'manager/manager_compa_list.html'
    model = Compa

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous or request.user.is_member:
            return redirect('no_authority')
        return super(ManagerCompaList, self).dispatch(request, *args, **kwargs)

class ManagerCompaNew(LoginRequiredMixin, CreateView):
    template_name = 'manager/manager_compa_form.html'
    model = Compa
    fields = ('comp_mode','hardware')
    success_url = reverse_lazy('manager_compa_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hards'] = Hardware.objects.all()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_member or request.user.is_anonymous:
            return redirect('no_authority')
        return super(ManagerCompaNew, self).dispatch(request, *args, **kwargs)

class ManagerCompaEdit(LoginRequiredMixin, UpdateView):
    template_name = 'manager/manager_compa_form.html'
    model = Compa
    fields = ('comp_mode','hardware')
    success_url = reverse_lazy('manager_compa_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hards'] = Hardware.objects.all()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous or request.user.is_member:
            return redirect('no_authority')
        return super(ManagerCompaEdit, self).dispatch(request, *args, **kwargs)

##유저
class ManagerUserList(LoginRequiredMixin, ListView):
    template_name = 'manager/manager_user_list.html'
    model = User

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous or request.user.is_member:
            return redirect('no_authority')
        return super(ManagerUserList, self).dispatch(request, *args, **kwargs)

##통계
class ManagerStat(LoginRequiredMixin, TemplateView):
    template_name = 'manager/manager_stat.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_member or request.user.is_anonymous:
            return redirect('no_authority')
        return super(ManagerStat, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hards'] = Hardware.objects.all()
        return context

#마이 페이지
class MemberHome(LoginRequiredMixin, TemplateView):
    template_name = 'member/member_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sets'] = Custom.objects.filter(user=self.request.user)[:10]
        context['ments'] = Comment.objects.filter(author=self.request.user)[:10]
        return context

# 함수형
def no_authority(request):
    return render(request, 'no_authority.html',{})

def portfolio_short(request):
    return render(request, 'portfolio_short.html', {})

@login_required
def leave(request):
    user = request.user
    user.delete()
    return redirect('leave_done')

def leave_done(request):
    return render(request, 'member/leave_done.html',{})

@login_required
def manager_hardware_remove(request, pk):
    some_hard = get_object_or_404(Hardware, pk=pk)
    if request.user.is_manager or request.user.is_superuser:
        some_hard.delete()
        return redirect('manager_hardware_list')
    else:
        return redirect('no_authority')

@login_required
def manager_compa_remove(request, pk):
    some_comp = get_object_or_404(Compa, pk=pk)
    if request.user.is_manager or request.user.is_superuser:
        some_comp.delete()
        return redirect('manager_compa_list')
    else:
        return redirect('no_authority')
#종류별 설명
def get_text(request):
    cpu = 'CPU는 컴퓨터의 연산장치로 컴퓨터의 뇌같은 하드웨어 입니다. 필수로 있어야만 컴퓨터를 조립할 수 있습니다.'
    borad = 'Board는 마더보드라고도 합니다. 보드가 있어야만 다른 하드웨어들을 장착할 수 있기때문에 필수입니다.'
    ram = 'RAM은 기억된 정보를 읽어내기도 하고 다른 정보를 기억시킬 수도 있는 메모리로서, 컴퓨터의 주기억장치, 응용 프로그램의 일시적 로딩과 데이터의 일시적 저장 등에 사용된다. 컴퓨터 작동을 위해서는 필수요소입니다.'
    vga = 'VGA는 그래픽카드입니다. 그래픽카드는 고사양을 필요로하는 게임과, 디자이너들이 사용합니다. 그래서 서핑과 컴퓨터에 적게 투자하여 이용하시고 싶으신 분들에게는 권장하지 않습니다.'
    power = 'Power는 컴퓨터의 전력을 공급하는 역할을 합니다. 필수로 있어야만 하는 하드웨어입니다. ex) 그래픽카드를 구매하시는 분들은 그래픽카드의 권장 정격과 파워의 정격을 확인하고 구매하시기 바랍니다.'
    hdd = 'HDD는 기억해야할 데이터를 기억해주는 역할을 합니다. 필수요소 입니다.'
    ssd = 'SSD는 HDD보다 빠른속도를 가지고 있습니다. 그래서 HDD보다 더 많이 사용되고 있습니다.'
    odd = 'ODD는 CD를 읽는 하드웨어입니다. 운영체재나 소프트웨어를 설치할때 사용합니다.'
    text = {
        'CPU':cpu,
        'Board':borad,
        'RAN':ram,
        'VGA':vga,
        'Power':power,
        'HDD':hdd,
        'SSD':ssd,
        'ODD':odd
    }
    return JsonResponse(text)

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
#메니저 페이지를 위한 정보 수집
def get_data(request):
    hardware = serializers.serialize('json', Hardware.objects.all())
    comp = serializers.serialize('json',Compa.objects.all())
    user = serializers.serialize('json',User.objects.all())
    date = {
        'hardware':hardware,
        'comp':comp,
        'user':user
    }
    return JsonResponse(date)
#아이디 중복검사
def get_id(request):
    users = User.objects.all()
    id = []
    for user in users:
        id.append(user.username)
    data = {
        'id':id
    }
    return JsonResponse(data)
# 전체 세트, 전체 댓글
def comment(request):
    comment = serializers.serialize('json', Comment.objects.all())
    id = serializers.serialize('json', User.objects.all())
    data = {
        'ment':comment,
        'id': id
    }
    return JsonResponse(data)
def set(request):
    set = serializers.serialize('json', Custom.objects.all())
    id = serializers.serialize('json', User.objects.all())
    data = {
        'set': set,
        'id': id
    }
    return JsonResponse(data)