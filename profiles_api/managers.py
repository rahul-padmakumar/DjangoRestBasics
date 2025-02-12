from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password):
        if not email:
            raise ValueError("Email required")
        email = self.normalize_email(email)
        model = self.model(email = email, name = name)
        model.set_password(password)
        model.save(using=self.db)
        return model
    
    def create_superuser(self, email, name, password):
        model = self.create_user(email, name, password)
        model.is_staff = True
        model.is_superuser=True
        model.save(using=self.db)
        return model
    