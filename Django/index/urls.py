from django.urls import path,include
from index.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', login_view, name='login'),
    path('register/',register_view, name='register'),

    path('logout/', UserLogout, name='logout'),

    path('admin/',admin_dashboard, name='admin'),

    path('products/', lista_productos, name='menu_food'),
    path('gestion_user/', include('index.modules.user.url')),
    path('gestion_product/', include('index.modules.products.url')),

    path('products/<int:producto_id>/', detalle_producto, name='detalle_producto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)