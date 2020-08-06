from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User, Client, Courier, Rest, Food


@admin.register(User)


class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'role', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'famil', 'mobil']
    list_filter = ['user', 'name' ]
    search_fields = ['name', 'famil']

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'famil', 'status', 'car']
    list_filter = ['user', 'name' ]
    search_fields = ['name', 'famil']
@admin.register(Rest)
class RestAdmin(admin.ModelAdmin):
    list_display = ['email', 'name_res', 'addres', 'category', 'discription']
    list_filter = ['user', 'name_res' ]
    search_fields = ['addres', 'name_res']
    

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['rest', 'name', 'price', 'category', 'image']
    list_filter = ['name', 'rest' ]
    search_fields = ['name', 'rest']
    
  