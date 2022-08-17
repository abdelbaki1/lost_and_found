from rest_framework import serializers 
from stuff.models import stuff
from Acounts.serializers import AcountSerializer
from Acounts.models import Acount
from images.serializer import ImageSerializer
 

class stuffSerializer(serializers.ModelSerializer):
    User = AcountSerializer(required=False)
    reference=serializers.IntegerField(read_only=True)
    class Meta:
        model = stuff
        fields='__all__'
    def create(self, validated_data):
        # create the location object
        #create the Category object
        # try:
            return stuff.objects.create(User=self.context['request'].user,**validated_data)
        # except:
            # raise ValueError("somthing went wrong")
class mainstuffSerializer(stuffSerializer):
    
    class Meta:
        model=stuff
        exclude=('date_found','description','location')
    
   



