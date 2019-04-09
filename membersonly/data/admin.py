from django.contrib import admin

from .forms import MemberForm
from .models import Member


class StatusAdmin(admin.ModelAdmin):
    list_display = ['a','b','c']
    form = MemberForm
    # class Meta:
    #     model = Status
        
        
admin.site.register(Member, StatusAdmin)