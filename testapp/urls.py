from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('views.HomeView.as_view()',name='home'),
    path('admin/', admin.site.urls),
]
