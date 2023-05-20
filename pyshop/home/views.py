from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
 
from home.models import Category
 
from .forms import CategoryForm
 
# Create your views here.
# def index(request: WSGIRequest) -> HttpResponse:
#     # category = Category(name="bruh")
#     # category.save()
#     categories = Category.objects.all()
#     return render(
#         request,
#         "home/index.html",
#         {
#             "title": "Home",
#             "categories": categories,
#         },
#     )
 
 
def catalog(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "home/catalog.html",
        {
            "title": "Catalog",
            "products": ["Product 1", "Product 2", "Product 3"],
        },
    )
 
 
class IndexView(ListView):
    template_name = "home/index.html"
    model = Category
    context_object_name = "categories"
 
 
class CategoryCreateView(CreateView):
    template_name = "home/category_create.html"
    form_class = CategoryForm

    # def post(self, request):
    #     form = CategoryForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         handle_uploaded_file(request.FILES["file"])
    #         return HttpResponseRedirect("/success/url/")
    #
    #     return render(request, "upload.html", {"form": form})
 
    def form_valid(self, form: CategoryForm) -> None:
        # print(dir(form))
        form.save()
        return redirect(to="/")
