from datetime import time, timedelta, datetime

""" Начальные данные """

dt_begin = time(9, 0)  # начало рабочего дня
dt_end = time(21, 0)  # конец рабочего дня
step = timedelta(minutes=30)  # длительность окна

busy = [
    {'start': '10:30',
     'stop': '10:50'
     },
    {'start': '18:40',
     'stop': '18:50'
     },
    {'start': '14:40',
     'stop': '15:50'
     },
    {'start': '16:40',
     'stop': '17:20'
     },
    {'start': '20:05',
     'stop': '20:20'
     }
]

list_windows = []

for i in busy:
    """ Преобразование времени в datetime.time() списка занятого времени в datetime.time() """
    i['start'] = time(*map(int, i['start'].split(':')))
    i['stop'] = time(*map(int, i['stop'].split(':')))

busy = sorted(busy, key=lambda x: x['start'])  # сортировка списка занятого времени


def check_time_in_busy(start, stop):
    """ Функция проверки окна на пересечение со списком занятого времени """
    for i in busy:
        if stop <= i['start']:
            break
        elif start >= i['stop']:
            continue
        else:
            return i['stop']
    return {'start': start.strftime('%H:%M'), 'stop': stop.strftime('%H:%M')}


while (datetime.combine(datetime.today(), dt_begin) + step).time() < dt_end:
    """ Цикл, передающий в функцию проверки окна начальное и конечное значение времени
     При возвращении из функции словаря - окно доступно и добавляется в список list_windows.
     При возвращении значения datetime.time (окончание занятого периода на данный интервал времени),
     оно присваивается начальному значению следующего интервала для повторной проверки """
    stop = (datetime.combine(datetime.today(), dt_begin) + step).time()
    check = check_time_in_busy(dt_begin, stop)
    if isinstance(check, dict):
        list_windows.append(check)
        dt_begin = (datetime.combine(datetime.today(), dt_begin) + step).time()
    else:
        dt_begin = check

print(list_windows)