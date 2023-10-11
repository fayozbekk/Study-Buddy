from django.contrib import admin
from .models import Category, RoomModel, Message, User


class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', "created", 'category')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Message)
admin.site.register(RoomModel, RoomAdmin)
