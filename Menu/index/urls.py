from django.urls import path,include
from index.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('gestion/', include('index.modules.user.url')),
]
