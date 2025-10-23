from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username',
                    'email',
                    'phone_number',
                    'address',
    ]
    
    fieldsets = UserAdmin.fieldsets + (("Delivery Information (Optional)", {"fields": ('address','phone_number',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Delivery Information (Optional)", {"fields": ('address','phone_number',)}),)

    
admin.site.register(CustomUser,CustomUserAdmin)


