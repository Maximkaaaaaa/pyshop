from django.urls import path
from .views import catalog, IndexView

urlpatterns = [
    # path('', index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('catalog/', catalog, name='catalog'),
]
