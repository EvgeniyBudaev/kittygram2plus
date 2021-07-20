# Администраторы сервера настоятельно попросили выделить им 2 часа в сутки
# (с трёх до пяти утра) на нагрузочное тестирование запросов к котикам.
# Они готовы работать ночью, но просят на это время запретить обработку
# запросов. В остальное время число обрабатываемых запросов должно
# лимитироваться, как и прежде. Для котиков — один запрос в минуту, для
# остальных эндпоинтов — в соответствии с настройками на уровне проекта.

from rest_framework import throttling

import datetime


class WorkingHoursRateThrottle(throttling.BaseThrottle):

    def allow_request(self, request, view):
        now = datetime.datetime.now().hour

        if now >= 3 and now <= 5:
            return False

        return True
