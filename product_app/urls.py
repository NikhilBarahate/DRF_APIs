from django.urls import path
from product_app.views import ProductMixinView

# Class Based:
urlpatterns = [
    path("<int:pk>/", ProductMixinView.as_view()),
    path("list/", ProductMixinView.as_view()),
    path("create/", ProductMixinView.as_view()),
]