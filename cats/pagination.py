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
#             'results': data
#         })


class CatsPagination(LimitOffsetPagination):
    default_limit = 1

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.count,
            'results': data
        })

#  limit - какое число объектов вернется
#  offset - с какого по счету объекта начать отсчёт
