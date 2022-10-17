from django.urls import path
from products.views import products, basket_add, basket_delete

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:category_id>', products, name='category'),
    path('page/<int:page>', products, name='page'),
    path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket_delete/<int:id>/', basket_delete, name='basket_delete')
]