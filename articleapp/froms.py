from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project



 
# 상속을받아서 >> 커스텀아이징 클래스

class ArticleCreationForm(ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable ',
                                                           'style': 'height:auto;text-align : left'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)




    # project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
 
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
        