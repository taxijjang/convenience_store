from django.urls import path

from . import views

app_name = "conveniences"

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="products"),
]
