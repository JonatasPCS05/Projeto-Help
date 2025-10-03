import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not re.search(r'[A-Z]', password):
            raise ValidationError(_("A senha deve conter pelo menos uma letra maiúscula."))
        if not re.search(r'[a-z]', password):
            raise ValidationError(_("A senha deve conter pelo menos uma letra minúscula."))
        if not re.search(r'\d', password):
            raise ValidationError(_("A senha deve conter pelo menos um número."))
        if not re.search(r'#[@$!%*?&.,;:_\-+=(){}[\]<>]', password):
            raise ValidationError(_("A senha deve conter pelo menos um caractere especial (@, $, !, %, etc)."))

    def get_help_text(self):
        return _(
            "Sua senha deve conter pelo menos: "
            "1 letra maiúscula, 1 letra minúscula, 1 número e 1 caractere especial."
        )
