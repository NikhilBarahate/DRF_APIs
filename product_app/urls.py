from django.urls import path
from product_app.views import (ProductDetailAPIView, product_create_apiview, 
                               product_list_apiview, product_list_create_apiview,
                               product_alt_view, product_update_apiview, product_destroy_apiview)


# Class Based:
urlpatterns = [
    path("<int:pk>/", ProductDetailAPIView.as_view()),
    path("create/", product_create_apiview),
    path("list/", product_list_apiview),
    path("list-create/", product_list_create_apiview),
    path("<int:pk>/update/", product_update_apiview),
    path("<int:pk>/delete/", product_destroy_apiview),

]

# Function Based.
# urlpatterns = [
#     path("<int:pk>/", product_alt_view),
#     path("", product_alt_view),
#     path("create/", product_alt_view),
#     path("list/", product_alt_view),
# ]