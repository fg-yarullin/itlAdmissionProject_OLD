import hashlib
import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from admin_profile.helpers.user_struct import get_scans
from admission.helpers.appeal_order import get_appeal_order
from admission.models import Participant
from first_tour.forms import UserAppealForm, TeacherAppealForm
from first_tour.models import Tour, UserAppeal, ExamResult, TourParticipantScan
from first_tour.task import test_celery
from itlAdmissionProject.settings import SALT, APPEAL_START_TIME, APPEAL_PERIOD_MINUTES


class AppealStruct:
    appeal: UserAppeal = None
    participant: Participant = None
    subjects = None
    tour: Tour = None
    formset = None
    scan: str = None
    appeal_time = None

    def __init__(self, participant, appeal, subjects, tour):
        self.participant = participant
        self.appeal = appeal
        self.subjects = subjects
        self.tour = tour
        self.formset = self.get_formset()
        self.scan = get_scans(participant=participant,
                              tour=tour)
        self.appeal_time = self.get_time()

    def get_formset(self):
        formSetQuery = ExamResult.objects.filter(participant=self.participant)
        FormSet = modelformset_factory(model=ExamResult, form=TeacherAppealForm, max_num=len(formSetQuery))
        formset = FormSet(queryset=formSetQuery)
        return formset

    def get_time(self):
        a = get_appeal_order(self.participant)
        appeal_order = APPEAL_START_TIME + datetime.timedelta(minutes=a * APPEAL_PERIOD_MINUTES)
        return appeal_order


@staff_member_required
def appeals_list(request):
    userAppeals = UserAppeal.objects.filter().order_by('appeal_apply_time', 'participant__last_name')
    results = []
    context = {
        'results': results,
    }

    if request.POST:
        key = list(request.POST.keys())[-1]
        participant = Participant.objects.get(pk=key)
        if request.POST[key] == '???? ????????????':
            ua = UserAppeal.objects.get(participant=participant)
            ua.is_absent_appeal = True
            ua.save()

    for ua in userAppeals:
        participant = ua.participant
        tour = ua.tour
        examResults = participant.examresult_set.filter(exam_subject__in=tour.examsubject_set.all()).order_by(
            'exam_subject__type_of_scoring')
        results.append(AppealStruct(participant=participant,
                                    appeal=ua,
                                    subjects=examResults,
                                    tour=tour
                                    )
                       )
        print(examResults)

    return render(request, 'first_tour/appeal_list.html', context=context)


@staff_member_required
def appeal_person(request, pk):
    # test_celery.delay(1)
    tour = Tour.objects.first()
    participant = Participant.objects.first()
    formSetQuery = ExamResult.objects.filter(participant_id=pk)
    FormSet = modelformset_factory(model=ExamResult, form=TeacherAppealForm, max_num=len(formSetQuery))
    formset = FormSet(queryset=formSetQuery)
    if request.POST:
        formset2 = FormSet(request.POST)
        print(formset.errors)
        if formset2.is_valid():
            formset2.save()
            return redirect('appeal-list')

    # print(tour.id)
    context = {
        'formset': formset,
        'pk': pk
    }
    # if request.POST:
    #     formset = FormSet(request.POST, queryset=formSetQuery)
    #     if formset.is_valid():
    #         formset.save()
    return render(request, 'first_tour/appeal_page.html', context=context)
