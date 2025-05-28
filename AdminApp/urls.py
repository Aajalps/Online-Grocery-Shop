from django.urls import path
from AdminApp import views

urlpatterns =[
    path("index/",views.index,name='index'),
    path("add_category/",views.add_category,name='add_category'),
    path("save_category/",views.save_category,name='save_category'),
    path("displaying_category/",views.displaying_category,name='displaying_category'),
    path("Edit_category/<int:pro_id>/",views.Edit_category,name='Edit_category'),
    path("update_category/<int:pro_id>/",views.update_category,name='update_category'),
    path("delete_category/<int:pro_id>/",views.delete_category,name='delete_category'),


    path("add_product/",views.add_product,name='add_product'),
    path("save_product/",views.save_product,name='save_product'),
    path("displaying_products/",views.displaying_products,name='displaying_products'),
    path("Edit_products/<int:pro_id>/",views.Edit_products,name='Edit_products'),
    path("update_product/<int:pro_id>/",views.update_product,name='update_product'),
    path("delete_products/<int:pro_id>/",views.delete_products,name='delete_products'),


    path("admin_login_page/",views.admin_login_page,name='admin_login_page'),
    path("admin_login/",views.admin_login,name='admin_login'),
    path("delete_logout/",views.delete_logout,name='delete_logout'),

    path("displaying_contact/",views.displaying_contact,name='displaying_contact'),
    path("delete_contact/<int:pro_id>/",views.delete_contact,name='delete_contact'),

    path("displaying_user/",views.displaying_user,name='displaying_user'),
    path("delete_user/<int:pro_id>/",views.delete_user,name='delete_user'),

    path('display_order/',views.display_order,name="display_order"),

    path("delete_order/<int:pro_id>/",views.delete_order,name='delete_order'),

    path('display_order2/',views.display_order2,name="display_order2"),

    path('delete_order2/<int:pro_id>/',views.delete_order2,name="delete_order2"),











]