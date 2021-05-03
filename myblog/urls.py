from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entradas/', include('entrys.urls')),
    path('cuentas/', include('accounts.urls'))
]
