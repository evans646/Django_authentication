from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# from .form import UserForm

# Create your views here.
def index(request):
    return render(request,'interface/index.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'  
    success_url = reverse_lazy('login')
  
    # def form_valid(self, form):
    #     valid = super(SignUp, self).form_valid(form)
    #     username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
    #     new_user = authenticate(username=username, password=password)
    #     login(self.request, new_user)
    #     return valid
    
    