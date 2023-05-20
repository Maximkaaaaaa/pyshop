from django.urls import path
from .views import catalog, IndexView, CategoryCreateView

urlpatterns = [
    # path('', index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('catalog/', catalog, name='catalog'),
    path('category/create/', CategoryCreateView.as_view(), name='categories_create')
]
