from rest_framework import serializers 
from app_api_tutorial.models import Tutorial
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = '__all__'