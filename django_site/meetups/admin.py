from django.contrib import admin
from .models import Meetup, Location, Participant

# Register your models here.

# class MeetupAdmin(admin.ModelAdmin):
#     list_display = ('title', 'date')
#     list_filter = ('title', 'date')
#     prepopulated_fields = {'slug':('title',)}


# admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Meetup)
admin.site.register(Location)
admin.site.register(Participant)
