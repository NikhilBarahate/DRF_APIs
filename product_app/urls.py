from django.urls import path
from product_app.views import product_list_create_apiview

# Class Based:
urlpatterns = [
    path("list/", product_list_create_apiview),
    path("create/", product_list_create_apiview),
]