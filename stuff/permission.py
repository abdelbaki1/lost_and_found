from rest_framework.permissions import  IsAuthenticated
class stuffPermision(IsAuthenticated):
    def has_object_permission(self,request,view,obj):
        super().has_object_permission(request,view,obj)
        return(obj.User==request.user)
     