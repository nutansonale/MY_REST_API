from rest_framework import serializers
from authenticate.models import Usersreg





class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usersreg
        fields=['User_name','user_email','passw']
