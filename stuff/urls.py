from django.urls import path
from .views import StuffView,StuffDetail,StuffDelete,StuffCreate,StuffUpdate,searchapi

urlpatterns = [
    path('main', StuffView.as_view(),name="main"),
    path('main/<int:ref>',StuffDetail().as_view(),name="detailedview"),
    path('stuff/delete/<int:ref>',StuffDelete.as_view(),name="stuffdelete"),
    path('stuff/create',StuffCreate.as_view(),name="stuffcreate"),
    path('stuff/update/<int:ref>',StuffUpdate.as_view(),name="stuffupdate"),
    path('test',searchapi.as_view(),name="test")
]