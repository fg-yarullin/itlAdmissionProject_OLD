from django.contrib import admin

# Register your models here.
from django.contrib.admin import TabularInline
from django.contrib.contenttypes.admin import GenericTabularInline

from admission.actions import export_as_xls, export_as_xls_full_participant_data
from admission.models import Profile, File, Participant, FirstTourDates, Group, Olympiad, Moderator, \
    ModeratorMessage, ParticipantRegistrator
from first_tour.action import export_results
from first_tour.models import Subject, Tour, ExamSubject, AppealUser, ExamResult, NextTourPass, UserAppeal, \
    TourParticipantScan, UploadConfirm, NextTourParticipantUpload, LiterGrade, AddLiter


class SubjectExamInlineAdmin(TabularInline):
    model = ExamSubject


@admin.register(Tour)
class AdminTour(admin.ModelAdmin):
    list_display = ('name', 'grade', 'profile', 'results_release_date', 'parent_tour', 'is_final_tour', 'tour_order')
    sortable_by = ('name', 'tour_order',)
    list_filter = (
        'results_release_date',)
    search_fields = ['name', 'results_release_date', 'parent_tour', 'is_final_tour']
    inlines = [
        SubjectExamInlineAdmin,
    ]
    actions = [export_results, ]

    # actions = [export_as_xls, export_as_xls_full_participant_data]

    # def get_email(self, participant):
    #     return str(participant.user.email)
    #
    # get_email.short_description = 'email'
    # get_email.admin_order_field = 'book__author'


@admin.register(ExamSubject)
class AdminExamSubject(admin.ModelAdmin):
    list_display = ('subject', 'tour', 'type_of_scoring', 'max_score', 'passing_score', 'ordering')
    sortable_by = ('tour', 'subject', 'ordering')
    list_filter = (
        'tour', 'type_of_scoring')
    search_fields = ['subject__name', ]


@admin.register(AppealUser)
class AppealUser(admin.ModelAdmin):
    list_display = ('user', 'tour')
    list_filter = ('tour',)


@admin.register(ExamResult)
class ExamResult(admin.ModelAdmin):
    list_display = ('participant', 'exam_subject', 'score', 'appeal_score')
    list_filter = ('exam_subject__tour',)


@admin.register(NextTourPass)
class NextTourPassAdmin(admin.ModelAdmin):
    list_display = ('participant', 'tour', 'type_of_pass')


@admin.register(TourParticipantScan)
class UserTourScanAdmin(admin.ModelAdmin):
    list_display = ('participant', 'tour', 'scan_file_name')
    list_filter = ('tour',)


@admin.register(UserAppeal)
class UserAppealAdmin(admin.ModelAdmin):
    list_display = ('participant', 'tour', 'appeal_apply_time', 'appeal_reason')
    list_filter = ('tour',)


@admin.register(UploadConfirm)
class UploadConfirmAdmin(admin.ModelAdmin):
    list_display = ('participant', 'tour', 'pps', 'agreement_tour')
    list_filter = ('tour',)


@admin.register(LiterGrade)
class LiterGradeAdmin(admin.ModelAdmin):
    list_display = ('tour', 'name')


admin.site.register(Subject)
admin.site.register(NextTourParticipantUpload)
admin.site.register(AddLiter)
