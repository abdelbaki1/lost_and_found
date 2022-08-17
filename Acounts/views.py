from rest_framework.permissions import  IsAuthenticated
from rest_framework.generics import CreateAPIView,UpdateAPIView,DestroyAPIView,ListAPIView
from .serializers import AcountSerializer
from .models import Acount
from stuff.models import stuff
from stuff.serializers import stuffSerializer
from rest_framework.pagination import PageNumberPagination
from knox.auth import TokenAuthentication
from .permissions import AcountPermission
class AcountCreate(CreateAPIView):
    serializer_class=AcountSerializer
class AcountUpdate(UpdateAPIView):
    http_method_names = ['patch', 'head', 'options', 'trace']
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,AcountPermission)
    serializer_class=AcountSerializer
    lookup_field='email'
    lookup_url_kwarg ='data'
    def get_queryset(self,*args,**kwargs):
        # super().get_queryset(*args,**kwargs)
        obj=Acount.objects.filter(email=self.kwargs[self.lookup_url_kwarg])
        return obj
class AcountDelete(DestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(AcountPermission,)
    lookup_field='email'
    lookup_url_kwarg ='data'
    def get_queryset(self,*args,**kwargs):
        # super().get_queryset(*args,**kwargs)
        obj=Acount.objects.filter(email=self.kwargs[self.lookup_url_kwarg])
        return obj
class AcountView(ListAPIView):#
    # this will be utilized for two view 
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AcountPermission,)
    serializer_class=stuffSerializer
    lookup_field='email'
    lookup_url_kwarg ='email'
    pagination_class=(PageNumberPagination)
   
    def get_queryset(self,*args,**kwargs):
        obj=stuff.objects.filter(User__email=self.kwargs[self.lookup_url_kwarg])
        return obj


