from django import forms
from django.contrib.auth import forms as fr, password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ClearableFileInput, TextInput, PasswordInput, EmailInput, RadioSelect, Select, DateInput, \
    CheckboxInput, Textarea, HiddenInput

from admission.models import File, Participant, GENDER_CHOICES, Group, ModeratorMessage
from first_tour.models import AppealUser, UserAppeal, ExamSubject, ExamResult, UploadConfirm


class UserAppealForm(forms.ModelForm):
    class Meta:
        model = UserAppeal
        exclude = ['is_absent_appeal']

        widgets = {
            'tour': HiddenInput(),
            'participant': HiddenInput(),
            'appeal_reason': Textarea(attrs={
                'placeholder': "Укажите, пожалуйста, предмет и причину аппеллирования."
            }),
            'appeal_apply_time': HiddenInput()
        }


class TeacherAppealForm(forms.ModelForm):
    subject_name = None

    def __init__(self, *args, **kwargs):
        super(TeacherAppealForm, self).__init__(*args, **kwargs)
        # self.fields['exam_subject'].widget.attrs['disabled'] = 'disabled'

        self.subject_name = self.instance.exam_subject.subject
        self.fields['appeal_score'].widget.attrs['required'] = 'required'

    class Meta:
        model = ExamResult
        fields = ('exam_subject', 'appeal_score')

        widgets = {
            'exam_subject': HiddenInput()
        }


class UserConfirmForm(forms.ModelForm):
    class Meta:
        model = UploadConfirm
        fields = ['tour', 'participant', 'pps', 'agreement_tour']
        widgets = {
            'tour': HiddenInput(),
            'participant': HiddenInput(),
            # 'pps': forms.FileInput(attrs={
            #     'placeholder': "",
            #     'class': 'form-control-file"'
            # }),
            # 'agreement_tour': forms.FileInput(attrs={
            #     'placeholder': "",
            #     'class': 'form-control-file"'
            # }),
        }

        # fields =