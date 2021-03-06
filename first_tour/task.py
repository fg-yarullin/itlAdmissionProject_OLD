import csv
import logging
import time

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from admin_profile.models import Error
from admission.models import Participant
from itlAdmissionProject.celery import app
from django.core.mail import send_mail, EmailMessage
from itlAdmissionProject.settings import SERVER_EMAIL


@app.task
def test_celery(x):
    # print('Started----------------')
    i = 0
    time.sleep(10)
    f = open('/Users/shuhrat/PycharmProjects/itlAdmissionProject/tmp44.txt', 'w')
    # print('Done')
    f.close()


@app.task
def make_mailing(email_subject, email_message, email):
    email = EmailMessage(email_subject,
                         email_message,
                         from_email=SERVER_EMAIL,
                         to=[email])
    email.send()


@app.task
def upload_liter(path, tour_ordering):
    from first_tour.models import LiterGrade

    with open(path) as File:
        reader = csv.DictReader(File)
        for row in reader:
            participant = Participant.objects.get(pk=row['id'])
            try:
                lg = LiterGrade.objects.get(tour__grade=participant.grade,
                                            tour__tour_order=tour_ordering,
                                            name=row['liter'])
                lg.participants.add(participant)
            except LiterGrade.DoesNotExist:
                error = Error()
                error.participant = participant
                error.message = 'Doesnt exists LiterGrade'
                error.save()
