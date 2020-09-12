from django.contrib import admin
from django.urls import path, include
from tasks.views import login_view, register_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/register/', register_view),
    path('tasks/login/', login_view),
    path('', include('tasks.urls')),
    path('tasks/logout/', logout_view),
]
