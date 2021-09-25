from . import views
from django.urls import path
urlpatterns = [
path('all/', views.PostListView.as_view(), name='all'),
path('<int:id>/',views.PostDetailView.as_view(), name='detail'),
path('blogger/<username>/',views.userpage, name='userpage')
]