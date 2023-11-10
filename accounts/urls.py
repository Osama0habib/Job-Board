from django.urls import path ,include
from . import views

app_name = 'accounts' 
urlpatterns = [
    path('login',views.signin,name='login'),
    path('signup',views.signup,name='sign_up'),
    path('profile',views.profile,name='profile'),
    path('profile/edit',views.profile_edit,name='profile_edit'),

]
  