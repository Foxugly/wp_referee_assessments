from django.contrib.auth.models import check_password
from users.models import CustomUser


class CustomUserBackend:

    # Create an authentication method

    def authenticate(self, username=None, password=None):

        try:
            user = CustomUser.objects.get(username=username)
            if check_password(password, user.password):
                return user
            else:
                return None
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None