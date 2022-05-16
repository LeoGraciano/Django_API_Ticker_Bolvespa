from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError(_('Um email válido deve ser informado.'))

        name = extra_fields.get('name')
        if not name:
            raise ValidationError('name deve ser informado')

        phone_number = extra_fields.get('phone_number')
        if not phone_number:
            raise ValidationError('phone_number deve ser informado')

        email = self.normalize_email(email)
        user = self.model(
            email=email, is_staff=is_staff,
            is_active=True, is_superuser=is_superuser,
            last_login=now, date_joined=now,
            name=name, phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,  email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user
