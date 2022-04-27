from django.contrib import admin
from .models import Dog, Exercise
# Register  models here.
admin.site.register(Dog) #allow crud updates for our dog table in our admin app
admin.site.register(Exercise)
admin.site.register(Toy)