from django.contrib import admin

# models
from accounts.models import User
from accounts.models import Profile
from accounts.models import Address


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('email','is_client','is_staff','is_active')
    search_fields=('email',)
    list_filter=('email','is_client')
    list_per_page=50

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','first_name','last_name','gender','date_of_join')
    search_fields=('user','first_name','date_of_join')
    list_filter=('gender','date_of_join')
    aw_id_fields=('user',)
    list_per_page=50

@admin.register(Address)
class PresentAddressAdmin(admin.ModelAdmin):
    list_display=('address_of','road','sector','police_station','city','district','post_code')
    search_fields=('address_of',)
    list_filter=('post_code','district',)
    list_per_page=50


