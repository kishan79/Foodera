from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('accounts/', include('accounts.urls')),
    path('', include('products.urls')),
    path('', include('cart.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
