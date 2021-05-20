import csv

from admission.models import Participant


def upload(path, tour):
    from first_tour.models import ExamResult, TourParticipantScan
    with open(path) as File:
        reader = csv.DictReader(File)
        exam_subjects = tour.examsubject_set.all()
        subj = []
        print(subj)
        results = []
        scans = []

        for row in reader:
            na = False
            try:
                participant = Participant.objects.get(id=row['id'])
            except:
                print('help')
            for esubj in exam_subjects:
                exam_result = ExamResult()
                print(participant)
                exam_result.participant = participant
                if row[esubj.subject.name] != '#N/A':
                    na = True
                    exam_result.score = float(row[esubj.subject.name].replace(',', '.'))
                else:
                    exam_result.score = 0
                exam_result.exam_subject = esubj
                results.append(exam_result)
            tscan = TourParticipantScan()
            tscan.participant = participant
            tscan.tour = tour
            tscan.scan_file_name = row['blank']
            if not na:
                scans.append(tscan)

        ExamResult.objects.bulk_create(results)
        TourParticipantScan.objects.bulk_create(scans)
        print(results)

    # print(path, tour.name)

# if __name__ == '__main__':
#     from first_tour.models import Tour
#
#     upload('/Users/shuhrat/Downloads/results.csv', Tour.objects.get('2'))
