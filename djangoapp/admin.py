from django.contrib import admin
from .models import HomeInfo
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class HomeAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(HomeInfo,HomeAdmin)