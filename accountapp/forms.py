from django.contrib.auth.forms import UserCreationForm



# 상속을받아서 >> 커스텀아이징 클래스

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields['username'].disabled = True
