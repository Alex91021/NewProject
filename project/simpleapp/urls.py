from django.urls import path
from .views import ProductsList, ProductDetail, CategorysList

urlpatterns = [path('categorys', CategorysList.as_view()),
               path('products', ProductsList.as_view()),
               path('<int:pk>', ProductDetail.as_view()),
               ]
