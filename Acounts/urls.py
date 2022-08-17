from django.urls import path
from .views import AcountCreate,AcountUpdate,AcountDelete,AcountView
from .auth import *
from knox.views import LogoutView

urlpatterns = [
    path('view/<str:email>',AcountView().as_view(),name="Acountview"),
    path('deleteview/<str:data>',AcountDelete().as_view(),name="AcountDelete"),
    path('createview',AcountCreate().as_view(),name="AcountCreate"),
    path('<str:data>/updateview',AcountUpdate().as_view(),name="AcountUpdate"),
    path('login',LoginView().as_view(),name="login"),
    path('logout',LogoutView().as_view(),name="logout")



    

]