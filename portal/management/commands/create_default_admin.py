from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Creates or resets a default admin user.'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv('DJANGO_ADMIN_USERNAME', 'admin')
        password = os.getenv('DJANGO_ADMIN_PASSWORD', 'admin1234')
        email = os.getenv('DJANGO_ADMIN_EMAIL', 'admin@example.com')

        user, created = User.objects.get_or_create(username=username, defaults={'email': email})
        user.email = email  # Always update email in case it changed
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)  # Always reset password
        user.save()
        if created:
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created with password '{password}'"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' password reset to '{password}' and email updated."))
