from django.urls import reverse, reverse_lazy
from django.http import*
from django.shortcuts import render
from accountapp.forms import AccountUpdateForm
from accountapp.models import MyTable
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    
    if request.method == 'POST':
        
        temp = request.POST.get("contnet_input")
        
        newMyTable = MyTable()
        newMyTable.text = temp
        newMyTable.save()
         
        newMyTable_list = MyTable.objects.all() # MyTable의 모든 데이터 긁어옴 
        
        # return render(request, 'accountapp/content.html', context={"newMyTable_list": newMyTable_list})
        # str1 = reverse('test')
        str2 = reverse('accountapp:test')
        print("str2 : {}".format(str2))
        return HttpResponseRedirect(reverse('accountapp:test'))
        
    else:
        newMyTable_list = MyTable.objects.all() # MyTable의 모든 데이터 긁어옴 
        
        return render(request, 'accountapp/content.html', context={"newMyTable_list": newMyTable_list})


class AccountCreateView(CreateView):
    model = User ## 장고에서 기본으로 지원하는 모델
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:test') # reverse든 lazy이든 (app, pathname)
    template_name = 'accountapp/create.html'
    
    
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' #쉽게말해서 이 클래스를 생성한 유저 (주인의 이름)
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User ## 장고에서 기본으로 지원하는 모델
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:test') # reverse든 lazy이든 (app, pathname)
    template_name = 'accountapp/update.html'