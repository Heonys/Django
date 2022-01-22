from django.forms import ModelForm
from articleapp.models import Article
 
# 상속을받아서 >> 커스텀아이징 클래스

class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
        