

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("404",views.Error404,name="404"),

    # <------------------- HomePage Url ---------------------------->
   
    # path('accounts/login/',auth_views.LoginView.as_view(template_name='homepage/login.html',authentication_form=LoginForm),name="login"),
    path('login/', views.admin_login,name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name="logout"),
    path('signup/', views.signup,name="signup"),

    # <------------------- END HomePage Url ---------------------------->


    # <-----------------Admin Dashboard------------------------>
    
    path('', views.home,name="home"),
    path('user/dashboard', views.user_dashboard,name="user_dashboard"),

    # <-----------------END Admin Dashboard------------------------>

    
    # <-------------------Admin Product---------------------------->

    path('product/add_product/', views.add_product.as_view(), name='add_product'),
    path('product/product-list',views.product_list,name="product_list"),
    path('product/product-delete/<str:pk>',views.product_delete,name="product_delete"),
    # path('product/edit-product',views.edit_product,name="edit_product"),

    # <-------------------End Admin Product---------------------------->

    # <-------------------Admin Accounts---------------------------->

    path('account/recharge_request',views.recharge_request,name="recharge_request"),
    path('account/recharge_status/<int:id>',views.recharge_status,name="recharge_status"),
    path('account/recharge_rejected/<int:id>',views.recharge_rejected,name="recharge_rejected"),
    path('account/withdraw_request',views.withdraw_request,name="withdraw_request"),

    path("recharge_list/", views.recharge_list,name="recharge_list"),
    # <-------------------END Admin Accounts---------------------------->

    # <------------------- UPI Admin ---------------------------->

    path("upi",views.add_upi.as_view(),name="add_upi"),
    path("upi/list",views.upi_list,name="upi_list"),


    # <-------------------END  UPI Admin ---------------------------->

    

    ############################ Profile Url ######################

    path("profile/",views.profile,name="profile"),
    path("user_list",views.user_list,name="user_list"),


    ############################ End Profile Url ######################
    path('kyc', views.add_kyc.as_view(), name='kyc'),
    path('kyc_list', views.kyc_list, name='kyc_list'),
    path('kyc_list_admin/', views.admin_kyc_list, name='admin_kyc_list'),
    # path("kyc",views.add_kyc,name="kyc"),
    ######################## User url #######################

    

    ######################## End User url #######################

    path("booking",views.booking,name="booking"),
    path("booking_list",views.booking_list,name="booking_list"),
    path("admin_booking_list",views.admin_booking_list,name="admin_booking_list"),


   
    # path('product/add_product/',views.add_product,name="add_product"),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


