# from django.shortcuts import render
from multiprocessing import context
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from profileapp.decorators import profile_ownership
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
from django.utils.decorators import method_decorator

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:test') # reverse든 lazy이든 (app, pathname)
    template_name = 'profileapp/create.html'


    def form_valid(self, form):
        temp = form.save(commit=False) # 만든 form을 불러와서 임시대기 
        temp.user = self.request.user
        temp.save()

        return super().form_valid(form)


@method_decorator(profile_ownership,'get')
@method_decorator(profile_ownership,'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:test') # reverse든 lazy이든 (app, pathname)
    template_name = 'profileapp/update.html'