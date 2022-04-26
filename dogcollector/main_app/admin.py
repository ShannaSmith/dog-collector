from django.contrib import admin
from .models import Dog
# Register your models here.
admin.site.register(Dog) #allow crud updates for our dog table in our admin app