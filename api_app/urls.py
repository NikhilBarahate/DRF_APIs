from django.urls import path
from api_app.views import first_api_view

urlpatterns = [
    path("", first_api_view)
]