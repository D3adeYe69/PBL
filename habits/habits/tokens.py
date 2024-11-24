from django.contrib.auth.tokens import PasswordResetTokenGenerator

class CustomTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.user_id) + str(timestamp) + str(user.email)

password_reset_token = CustomTokenGenerator()