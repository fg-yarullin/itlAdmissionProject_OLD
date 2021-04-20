from django.contrib import admin

# Register your models here.
from django.contrib.admin import TabularInline
from django.contrib.contenttypes.admin import GenericTabularInline

from admission.models import Grade, Profile, File, Participant, FirstTourDates, Group, Olympiad


class FileAdmin(TabularInline):
    model = Participant.portfolio.through


@admin.register(Grade)
class AdminGrade(admin.ModelAdmin):
    list_display = ('number', 'profile_id')
    sortable_by = ('number', 'profile_id')


@admin.register(Participant)
class AdminParticipant(admin.ModelAdmin):
    list_display = ('user', 'last_name', 'first_name', 'fathers_name', 'grade', 'profile')
    sortable_by = ('grade', 'last_name', 'first_name')
    list_filter = ('grade', 'profile', 'first_tour_register_date')
    search_fields = ['first_name', 'last_name']
    exclude = ['portfolio']
    inlines = [
        FileAdmin,
    ]


admin.site.register(File)
admin.site.register(FirstTourDates)
admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Olympiad)
