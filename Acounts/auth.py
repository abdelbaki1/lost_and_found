from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView


class LoginView(KnoxLoginView):
    
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        print(request.user)
        return super(LoginView, self).post(request, format=None)
class LogoutView(LogoutView):
    '''mark the last date of login and some other things'''
    pass