from django.shortcuts import render
import datetime


def main(request):
    """
    Вначале находим кол-во недель между датами, затем проверяем является ли
    день понедельником.
    """
    context = {}
    if request.method == 'POST' and len(request.POST['date']) != 0:
        date_from_request = request.POST['date'].split('-')
        date_start = datetime.date(2019, 1, 1)
        date_end = datetime.date(*[int(i) for i in date_from_request])
        if date_end < date_start:
            context['weeks'] = 'Выберите дату после 01.01.2019'
        else:
            weeks = (date_end - date_start).days // 7 + 1
            if date_end.isocalendar()[2] == 1:
                weeks += 1
            context['weeks'] = weeks
    return render(
        request, 'index.html', context
    )
