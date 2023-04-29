from django.shortcuts import render


def index(request):
    return render(request, "home/index.html", {
        "title": "Home",
        "name": "Vova",
    })


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