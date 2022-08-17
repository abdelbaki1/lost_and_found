from rest_framework import serializers 
from Acounts.models import Acount
 
class AcountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Acount
        fields=['first_name','last_name','email','date_joined','phone','password']
        extra_kwargs={'email':{'validators':[]},'password':{'validators':[]}}
        optionel_fields=['password',]
        
    def create(self, validated_data):
        print('create methode has been hitten')
        Object=Acount.objects.create(**validated_data)
        Object.set_password(validated_data['password'])
        Object.save()
        return Object
    def update(self,instance,validated_data):
        password=validated_data.get("password",False)
       
        print(password)
        if password != False:
            instance.set_password(validated_data['password'])
            print(f"value has changed {password}")
            validated_data.pop('password')
        for k in validated_data.keys():
            print(f"value has changed {k}")
            setattr(instance,k,validated_data.get(k,getattr(instance,k)))
        instance.save()
        return instance

        

