from django.urls import path,include
from .views import TagCreateList,TagDetail,CategoryViewSet,ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryViewSet)
# router.register('product', ProductViewSet)

urlpatterns = [
    path('tags/',TagCreateList.as_view(),name='tag_create'),
    path('tags/<int:id>/',TagDetail.as_view(),name='tag'),
    path("",include(router.urls)),
    path('products/',ProductViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    ),name='products'),
    path('products/<int:id>/',ProductViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}
    ))
]
"""
pip install drf-spectacular
"""