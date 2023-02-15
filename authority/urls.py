from django.urls import path

# views
from authority.views import admin_main

app_name = 'authority'

urlpatterns = [
    path('authority', admin_main.AdminHomeView.as_view(), name="authority"),
    
]
