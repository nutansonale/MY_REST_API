from rest_framework import serializers
from requests.models import ProjectCreateQ

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectCreateQ
        fields=['sid','user_name','dimage','status']


        