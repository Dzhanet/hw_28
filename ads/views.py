from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

from ads.models.ad import Ad
from ads.models.category import Category
from ads.serializers import AdSerializer, CatSerializer

from django.http import JsonResponse


def index(request):
    response = {'status': 'ok'}
    return JsonResponse(response, status=200)


class AdViewSet(viewsets.ModelViewSet):
    """ Для списка объявлений"""
    queryset = Ad.objects.filter(is_published=True)
    serializer_class = AdSerializer

    # def get_queryset(self):
    #     """ Возвращает определенное количество записей"""
    #     pk = self.kwargs.get('pk')
    #     if not pk:
    #         return Ad.objects.all()[:3]
    #     return Ad.objects.filter(pk=pk)
    #
    # @action(methods=['GET'], detail=False)  # detail - Для списка записей, если True -тогда одна запись.
    # def category(self, request):
    #     """ Добавление не стандартных маршрутов в класс AdsViewSet, localhost/ad/category"""
    #     cats = Category.objects.all()
    #     return JsonResponse({'cats': [cat.name for cat in cats]}, json_dumps_params={"ensure_ascii": False})


class CatViewPagination(PageNumberPagination):
    """ Для категорий свой класс пагинации"""
    page_size = 2
    # page_size - Доп параметр в get запросе например  http://localhost/cat/?page_size=5
    page_size_query_param = 'page_size'
    # Максимальное значение для 'page_size'
    max_page_size = 10


class CatViewSet(viewsets.ModelViewSet):
    """ Для списка категорий"""
    queryset = Category.objects.all().order_by('name')
    serializer_class = CatSerializer
    pagination_class = CatViewPagination
