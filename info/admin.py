from django.contrib import admin
from .forms import UserRegisterForm

from .models import *

admin.site.register(skills)
admin.site.register(position)
admin.site.register(vacant_position)
admin.site.register(user_details)




