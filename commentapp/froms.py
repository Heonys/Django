from django.forms import ModelForm
from commentapp.models import Comment
 
# 상속을받아서 >> 커스텀아이징 클래스

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        