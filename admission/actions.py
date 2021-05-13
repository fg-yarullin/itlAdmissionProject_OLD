from openpyxl import Workbook
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from datetime import datetime, date
from action_export.export_excel import ExportExcelAction
from openpyxl.styles import Font
from unidecode import unidecode


def get_value(obj):
    if obj is None:
        return ''
    return str(obj)


def style_output_file(file):
    black_font = Font(color='000000', bold=True)
    for cell in file["1:1"]:
        cell.font = black_font

    for column_cells in file.columns:
        print([cell.value for cell in column_cells])
        length = max(len(cell.value) for cell in column_cells)
        length += 10
        file.column_dimensions[column_cells[0].column_letter].width = length

    return file


def convert_data_date(value):
    return value.strftime('%d/%m/%Y')


def convert_boolean_field(value):
    if value:
        return 'Yes'
    return 'No'


def export_as_xls(self, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    opts = self.model._meta
    field_names = self.list_display
    file_name = unidecode(opts.verbose_name)
    blank_line = []
    wb = Workbook()
    ws = wb.active
    ws.append(ExportExcelAction.generate_header(self, self.model, field_names))

    for obj in queryset:
        row = []
        for field in field_names:
            is_admin_field = hasattr(self, field)
            if is_admin_field:
                value = getattr(self, field)(obj)
            else:
                value = getattr(obj, field)
                if isinstance(value, datetime) or isinstance(value, date):
                    value = convert_data_date(value)
                elif isinstance(value, bool):
                    value = convert_boolean_field(value)
            row.append(str(value))
        ws.append(row)

    ws = style_output_file(ws)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={file_name}.xlsx'
    wb.save(response)
    return response


export_as_xls.short_description = "Export short info as excel"
exclude_fields = ['portfolio_text', 'portfolio', 'moderatormessage']


def export_as_xls_full_participant_data(self, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    header = [
        'ID',
        'ФАМИЛИЯ',
        'ИМЯ',
        "ОТЧЕСТВО",
        'Номер телефона абитуриента',
        'EMAIL',
        'ФИО МАМЫ',
        'Номер МАМЫ',
        'ФИО ОТЦА',
        'НОМЕР ОТЦА',
        'КЛАСС',
        'Профиль',
        'Школа',
        'Дата первого тура'
    ]

    wb = Workbook()
    ws = wb.active
    ws.append(header)

    for participant in queryset.order_by('last_name', 'first_name', 'fathers_name', 'grade'):
        if not participant.is_dublicate and participant.first_name is not None:
            ws.append([
                str(participant.pk),
                participant.last_name,
                participant.first_name,
                participant.fathers_name,
                participant.phone_party,
                participant.user.email,
                get_value(participant.fio_mother),
                get_value(participant.phone_mother),
                get_value(participant.fio_father),
                get_value(participant.phone_father),
                get_value(participant.grade.number),
                'Нет' if participant.profile is None else participant.profile.name,
                participant.school,
                str(participant.first_tour_register_date)
            ])
    ws = style_output_file(ws)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=Participants.xlsx'
    wb.save(response)
    return response


export_as_xls_full_participant_data.short_description = 'Export full db'
