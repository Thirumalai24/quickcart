from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login_page, name="login"),
    path('logout', views.logout_page, name="logout"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('cart', views.cart_page, name="cart"),
    path('remove_cart/<str:cid>', views.remove_cart, name="remove_cart"),
    path('fav',views.add_to_fav,name="fav"),
    path('favviewpage',views.fav_view_page,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:name>', views.collectionsview, name="collections"),
    path('collections/<str:cname>/<str:pname>', views.product_details, name="product_details")

]
