from django.urls import path,include
from index.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogout, name='logout'),

    path('products/', lista_productos, name='menu_food'),
    path('gestion_user/', include('index.modules.user.url')),
    path('gestion_product/', include('index.modules.products.url')),
]
