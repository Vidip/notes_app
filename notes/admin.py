from django.contrib import admin
from models import user_profile, user_notes

# Register your models here.
admin.site.register(user_profile)
admin.site.register(user_notes)