from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from home.models import Category


#
# def index(request):
#     return render(request, "home/index.html", {
#         "title": "Home",
#         "name": "Vova",
#     })


def catalog(request):
    context = {
        "title": "Home",
        "products": [
            "Notebooks",
            "Phones",
            "Monitors",
        ]
    }
    return render(request, "home/catalog.html", context=context)


# class IndexView(View):
#     def get(self, request):
#         return render(request, "home/index.html", {
#             "title": "Home",
#             "name": "Vova",
#         })

class IndexView(ListView):
    template_name = "home/index.html"
    model = Category
    context_object_name = 'categories'
