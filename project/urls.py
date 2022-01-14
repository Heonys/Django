from django.contrib import admin
from django.urls import path, include

import accountapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accountapp.urls'))
]
 
 
