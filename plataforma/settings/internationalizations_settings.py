from django.utils.translation import gettext_lazy as _

# Default Language
LANGUAGE_CODE = 'pt-br'

DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True

# Supported Language
LANGUAGES = [
    ('pt-br', _('Brazilian Portuguese')),
    ('en', _('English')),
]

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True
