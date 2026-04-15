from django.shortcuts import render

"""
Class Based Views и mixins в DRF.
"""
from rest_framework import mixins,generics
from .models import Tag
from .serializers import TagSerializer

class TagCreateList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class TagDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request,*args,**kwargs)

"""
ViewSets, routers, пагинация.filters
"""
from rest_framework import viewsets

from .serializers import CategorySerializer,ProductSerializer
from .models import Category,Product

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

class ProductPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filter_fields = ['category',"status","is_active"]
    search_fields = ['title',"price"]
    ordering_fields = ["price","created"]
    ordering = ["-created"]

    def get_queryset(self):
        return ( Product.objects
                 .select_related('category')
                 .prefetch_related('tags')
                 )