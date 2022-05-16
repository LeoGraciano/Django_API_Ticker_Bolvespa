from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


from accounts.manager import UserManager
from core.models import BaseModelField


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        _('E-mail'), unique=True,
        db_column='email'
    )
    name = models.CharField(
        _('Nome completo'), max_length=150,
        db_column='name'
    )
    phone_number = models.CharField(
        _('Telefone celular'),
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^[1-9]{2}9[0-9]{8}$',
                message=_('Telefone inválido')
            )
        ],
        db_column='phone_number'
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now)
    is_trusty = models.BooleanField(default=False)
    confirmation_key = models.CharField(
        max_length=24,
        blank=True, null=True,
        db_column='confirmation_key'
    )
    created_at = models.DateField(
        _('Created in'), auto_now_add=True,
        db_column='created_at'
    )
    updated_at = models.DateField(
        'Updated in', auto_now=True,
        db_column='updated_at'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']



    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.full_clean()  # Verifica as restrições extras de cada field
        super().save(*args, **kwargs)

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def short_name(self):
        return self.name.split(' ')[0]




