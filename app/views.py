from django.shortcuts import render,redirect,get_object_or_404
from django.urls.resolvers import URLPattern 
from django.views.generic import ListView,DetailView
from .forms import ProfileEditForm

from .models import Post,Profile,User
# Create your views here.
class PostListView(ListView):
    model=Post
    paginate_by=5
    template_name='allblogs.html'
class PostDetailView(DetailView):
    model=Post
    template_name='blogdetail.html'
    pk_url_kwarg='id'
def userpage(request,username):
    user=User.objects.get(username=username)
    posts=Post.objects.filter(author=user) #все посты автора
    profile=Profile.objects.get(user=user) #профиль автора
    return render(request, 'profilepage.html',{'user': user,
     'posts':posts, 'profile': profile} )


def allblogers(request):
    users=User.objects.all()
    return render(request, 'allusers.html', {'users':users})
    


