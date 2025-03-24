from django.contrib.auth.backends import BaseBackend
from .models import User



class UserAuthenticationBackend(BaseBackend):
    
    def authenticate(self, request, username = None, password = None, **kwargs):
        try:
            shop = User.objects.get(email=username)
            if shop.check_password(password):
                return shop
        except User.DoesNotExist:
            return None
        
    def get_user(self,shop_id):
        try:
            return User.objects.get(pk = shop_id)
        except User.DoesNotExist:
            return None
