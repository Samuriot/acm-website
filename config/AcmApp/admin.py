from django.contrib import admin
from .models import Members, Events, Officers, Comments
# Register your models here.



@admin.register(Members)
class MemberAdmin(admin.ModelAdmin):
    pass

@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(Officers)
class OfficerAdmin(admin.ModelAdmin):
    pass

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    pass