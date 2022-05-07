from django.shortcuts import render
import datetime


def main(request):
    """
    Вначале находим кол-во недель между датами, затем проверяем является ли
    день понедельником.
    """
    context = {}
    if request.method == 'POST':
        date_from_request = request.POST['date'].split('-')
        date_start = datetime.date(2019, 1, 1)
        date_end = datetime.date(*[int(i) for i in date_from_request])
        weeks = (date_end - date_start).days // 7 + 1
        if date_end.isocalendar()[2] == 1:
            weeks += 1
        context['weeks'] = weeks
    return render(
        request, 'index.html', context
    )
