from rest_framework.pagination import (PageNumberPagination,
                                       LimitOffsetPagination)
from rest_framework.response import Response


# class CatsPagination(PageNumberPagination):
#     page_size = 1
#
#     def get_paginated_response(self, data):
#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#             },
#             'count': self.page.paginator.count,
#             'response': data
#         })


class CatsPagination(LimitOffsetPagination):
    default_limit = 2

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.count,
            'response': data
        })

#  limit - какое число объектов вернется
#  offset - с какого по счету объекта начать отсчёт
#  GET http://127.0.0.1:8000/cats/?limit=2&offset=4
#  Такой GET-запрос вернёт два объекта, с пятого по шестой
#  (или меньше, если в результате запроса менее 6 объектов).
