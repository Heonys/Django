from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from articleapp.models import Article
from django.views.generic.list import MultipleObjectMixin

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})


    def form_valid(self, form):
        temp = form.save(commit=False) # 만든 form을 불러와서 임시대기 
        temp.user = self.request.user
        temp.save()

        return super().form_valid(form)




class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project' #쉽게말해서 이 클래스를 생성한 유저 (주인의 이름)
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, **kwargs)

    




class ProjectListView(ListView):
    model = Project 
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25

