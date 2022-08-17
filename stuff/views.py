from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from knox.auth import TokenAuthentication
from .permission import stuffPermision  # <-- Here
from rest_framework.permissions import  IsAuthenticated,IsAuthenticatedOrReadOnly
from .models import stuff
from rest_framework.pagination import PageNumberPagination
from .serializers  import *
from images.models import Image
from images.serializer import ImageSerializer
from rest_framework.response import Response
from rest_framework import filters

class StuffView(ListAPIView):
    
    pagination_class=PageNumberPagination
    model=stuff
    serializer_class=mainstuffSerializer

   
    def get_queryset(self,*args,**kwargs):
        # super().get_queryset(*args,**kwargs)
        obj=self.model.objects.order_by('-date_created')
        return obj
  
class StuffDetail(RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field='reference'
    lookup_url_kwarg='ref'
    serializer_class=stuffSerializer
    queryset=stuff.objects.all()
    def retrieve(self, request, *args, **kwargs):

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        Images=ImageSerializer(Image.objects.filter(stuff__reference=str(self.kwargs[lookup_url_kwarg])),many=True)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response=serializer.data
        response['images']=Images.data
        
        

        return Response(response)

    
   
class StuffCreate(CreateAPIView):
    serializer_class=stuffSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
             
class StuffUpdate(UpdateAPIView):
    serializer_class=stuffSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (stuffPermision,)
    lookup_field='reference'
    lookup_url_kwarg='ref'
    def get_queryset(self,*args,**kwargs):
        # super().get_queryset(*args,**kwargs)
        obj=stuff.objects.filter(User=self.request.user)
        return obj
class StuffDelete(DestroyAPIView):
    serializer_class=stuffSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (stuffPermision,)
    lookup_field='reference'
    lookup_url_kwarg='ref'
    def get_queryset(self,*args,**kwargs):
        # super().get_queryset(*args,**kwargs)
        obj=stuff.objects.filter(User=self.request.user)
        return obj
class searchapi(ListAPIView):
    serializer_class=stuffSerializer
    pagination_class=PageNumberPagination
    queryset=stuff.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['description', 'name']

    


