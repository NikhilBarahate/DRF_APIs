from django.urls import path
from product_app.views import model_instance_view

urlpatterns = [
    path("", model_instance_view)
]