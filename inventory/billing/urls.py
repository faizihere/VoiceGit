from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('temp', views.temp, name='temp'),
    path('loginAction', views.loginAction, name='loginAction'),
    path('logoutAction', views.logoutAction, name='logoutAction'),
    path('entityRegistration', views.entityReg, name='entityreg'),
    path('registerAction', views.registerAction, name='registerAction'),

    path('supplierAction', views.supplierAction, name='supplierAction'),
    path('addSupplier',views.addSupplier, name='addSupplier'),

    path('productAction', views.productAction, name='productAction'),
    path('addProduct', views.addProduct, name='addProduct'),

    path('billProduct', views.billProduct, name='billProduct'),

    path('branchManagerReg', views.branchManagerReg, name='branchManagerReg'),
    path('counterManagerReg', views.counterManagerReg, name='counterManagerReg'),

    path('managerDashboard', views.managerDashboard, name='managerDashboard'),
    
    path('billClear',views.billClear,name='billClear'),

    path('billConfirm',views.billConfirm,name='billConfirm'),

    path('cashierDash',views.cashierDash,name='cashierDash'),
    path('branchManagerDash',views.branchManagerDash,name='branchManagerDash'),
    path('entityDirectorDash',views.entityDirectorDash,name='entityDirectorDash'),


]
