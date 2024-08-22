from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from books.views import *
from reviews.views import *
from carts.views import CartView
from orders.views import *
from stores.views import StoreListView
from customers.views import CustomerLoginAPI, CreateUserView
from .yasg import urlpatterns as doc_urls


router = SimpleRouter()
# router.register(r"api/v1/stores", StoreViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/book/<int:pk>', BookDetailView.as_view()),
    path('api/v1/book-list', BookListView.as_view()),
    path('api/v1/add-review/<int:book_id>', BookCreateReviewView.as_view()),
    path('api/v1/book-reviews/<int:book_id>', BookReviewsListView.as_view()),
    path('api/v1/profile/reviews', CustomerReviewsListView.as_view()),
    path('api/v1/carts', CartView.as_view()),
    path('api/v1/orders', OrderListView.as_view()),
    path('api/v1/order/<int:order_id>', OrderRetrieveView.as_view()),
    path('api/v1/order', OrderCreateView.as_view()),
    path('api/v1/stores', StoreListView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]

urlpatterns += doc_urls

urlpatterns += router.urls
