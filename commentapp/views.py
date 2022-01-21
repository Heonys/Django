from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import*
from django.views.generic import CreateView, DetailView
from articleapp.models import Article
from commentapp.models import Comment
from commentapp.froms import CommentCreationForm


# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp = form.save(commit=False) # 만든 form을 불러와서 임시대기 
        temp.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp.writer = self.request.user
        temp.save()

        return super().form_valid(form)


    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})


