from django.shortcuts import render
import datetime


START_YEAR_DATE = datetime.date(2019, 1, 1)
START_WEEK_DATE = datetime.date(2019, 1, 5)


def main(request):
    """
    Так как неделя съехала на 6 дней, то прибавим 6 к разности дат,
    кроме того, так как мы отдельно проверяем находится ли наша дата в промежутке между
    1-ми и 5-ми числами, то не забудем прибавить 1.
    В программе присутствуют две переменные начала, одна отвечает за дату начала года,
    другая за начало второй недели.
    Получаем формулу:
    (полученная_дата - дата_начала_второй_недели + 6(т.к. новая неделя начинается с воскресенья)) //
    // 7 + 1 (т.к. используя дату_начала_второй_недели, забываем про первую)
    """
    context = {}
    if request.method == 'POST' and request.POST['date']:
        date_from_request = request.POST['date'].split('-')
        date_end = datetime.date(*[int(i) for i in date_from_request])
        if date_end < START_YEAR_DATE:
            weeks = 'Выберите дату после 01.01.2019'
        elif START_YEAR_DATE <= date_end <= START_WEEK_DATE:
            weeks = 1
        else:
            weeks = ((date_end - START_WEEK_DATE).days + 6) // 7 + 1
        context['weeks'] = weeks
    return render(
        request, 'index.html', context
    )

