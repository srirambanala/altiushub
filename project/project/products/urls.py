from django.urls import path
from .views import HomePage, update_product, delete_product ,search_results

app_name = 'products'
#url partterns for products app
urlpatterns = [
    path('',HomePage, name='home'),
    path('update/<int:id>', update_product , name='update'),
    path('delete/<int:id>', delete_product, name='delete'),
    path('search/<str:query>/', search_results, name='search_results'),]

