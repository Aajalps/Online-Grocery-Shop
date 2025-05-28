from django.urls import path
from WebApp import views

urlpatterns =[
    path("homePage/",views.homePage,name="homePage"),
    path("aboutpage/", views.aboutpage, name="aboutpage"),
    path("contactpage/", views.contactpage, name="contactpage"),
    path("save_contact/", views.save_contact, name="save_contact"),
    path("productpage/", views.productpage, name="productpage"),
    path("filtered_product/<cat_name>/", views.filtered_product, name="filtered_product"),
    path("single_product/<int:pro_id>/", views.single_product, name="single_product"),
    path("", views.user_reg, name="user_reg"),
    path("user_log/", views.user_log, name="user_log"),
    path("save_reg/", views.save_reg, name="save_reg"),

    path("user_login/", views.user_login, name="user_login"),
    path("delete_user/", views.delete_user, name="delete_user"),
    path("cart/", views.cart, name="cart"),
    path("save_cart/", views.save_cart, name="save_cart"),

    path("delete_Cart/<int:pro_id>/", views.delete_Cart, name="delete_Cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("save_bill/", views.save_bill, name="save_bill"),
    path("payment/", views.payment, name="payment"),

]