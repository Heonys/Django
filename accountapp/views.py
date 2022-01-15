from django.shortcuts import render

from accountapp.models import MyTable


# Create your views here.

def index(request):
    
    if request.method == 'POST':
        
        temp = request.POST.get("contnet_input")
        
        newMyTable = MyTable()
        newMyTable.text = temp
        newMyTable.save()
         
        newMyTable_list = MyTable.objects.all() # MyTable의 모든 데이터 긁어옴 
        
        return render(request, 'accountapp/content.html', context={"newMyTable_list": newMyTable_list})
    else:
        return render(request, 'accountapp/content.html', context={"newMyTable_list": '이상한데'})
