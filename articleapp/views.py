from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from articleapp.decorators import article_ownership
from articleapp.froms import ArticleCreationForm
from articleapp.models import Article
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import*
from django.views.generic.edit import FormMixin
from commentapp.froms import CommentCreationForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})


    def form_valid(self, form):
        temp = form.save(commit=False) # 만든 form을 불러와서 임시대기 
        temp.writer = self.request.user
        temp.save()

        return super().form_valid(form)


class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article' #쉽게말해서 이 클래스를 생성한 유저 (주인의 이름)
    template_name = 'articleapp/detail.html'



@method_decorator(article_ownership, 'get')
@method_decorator(article_ownership, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})




@method_decorator(article_ownership, 'get')
@method_decorator(article_ownership, 'post')
class ArticleDeleteView(DeleteView):
    model = Article 
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list') 
    template_name = 'articleapp/delete.html'




class ArticleListView(ListView):
    model = Article 
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 10
