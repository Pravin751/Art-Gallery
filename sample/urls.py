"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from app import views 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as app_views
 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('forgotconfirm/',views.forgotconfirm,name="forgotconfirm"),
    path('',views.home,name="home"),
    path('index/',views.index,name="index"),
    path('user_register/',views.user_register,name="user_register"),
    
    path('login/',views.login,name="login"),
    path("change_password/",views.change_password,name="change_password"),
    path('home/',views.logout,name="logout"),
    path('ArtistAccountt/',views.ArtistAccountt,name="ArtistAccountt"),
    path('Singleproduct/<int:jk>/',views.Singleproduct ,name="Singleproduct"),
    path('allproduct/',views.allproduct ,name="allproduct"),
    path('my_products/',views.my_products ,name="my_products"),
    path("update_product/",views.update_product, name="update_product"),
    path("delete_product/",views.delete_product, name="delete_product"),
    
    path("cart",views.cart1,name="cart"),
    path("get_cart_data",views.get_cart_data,name="get_cart_data"),
    path("change_quan",views.change_quan,name="change_quan"),
    path('profile/',views.profile,name="profile"),
    path('profile33/',views.profile33,name="profile33"),
    path('add_user/',views.add_user,name="add_user"),
    path('add_post/',views.add_post,name="add_post"),
    path('user_edit/<int:pk>/',views.user_edit,name="user_edit"),
    path('user_delete/<int:a>/',views.user_delete,name="user_delete"),
    path('reset_password/',app_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/',app_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',app_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',app_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('process_payment/',views.process_payment,name="process_payment"),
    path('payment_done/',views.payment_done,name="payment_done"),
    path('payment_cancelled/',views.payment_cancelled,name="payment_cancelled"),
    path('order_history/',views.order_history,name="order_history"),
    path('my_customer/',views.my_customer,name="my_customer"),
    path('register12/',views.register12,name="register12"),
    path("cust_dashboard/",views.cust_dashboard,name="cust_dashboard"),
    path("photopainting/",views.photopainting,name="photopainting"),
    path("seller/",views.seller,name="seller"),
    path("photoconvert/",views.photoconvert,name="photoconvert"),



    
]    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

