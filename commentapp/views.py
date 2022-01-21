from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import*
from django.views.generic import CreateView, DeleteView
from articleapp.models import Article
from commentapp.decorators import comment_ownership
from commentapp.models import Comment
from commentapp.froms import CommentCreationForm


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


@method_decorator(comment_ownership, 'get')
@method_decorator(comment_ownership, 'post')
class CommentDeleteView(DeleteView):
    model = Comment 
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})