
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('crm_app.urls'))
]


handler404 = 'crm_app.views.Error404'
