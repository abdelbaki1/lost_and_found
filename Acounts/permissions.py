from rest_framework.permissions import  IsAuthenticated
class AcountPermission(IsAuthenticated):
    def has_object_permission(self,request,view,obj):
        super().has_object_permission(request,view,obj)
        
        # try:
        print("you're good to to go")
        return(obj.email==request.user.email)
        # except:
        #     print('unable to verify')
        #     return()
     