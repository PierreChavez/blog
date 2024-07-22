from rest_framework.serializers import ModelSerializer
from users.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'password', 'last_login', 'is_superuser', 'username',
            'first_name', 'last_name', 'is_staff', 'is_active',
            'date_joined', 'email', 'web_site', 'groups', 'user_permissions'
        ]
        #fields = '__all__'