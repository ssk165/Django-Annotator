from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class CharacterSet(models.Model):
    regex = models.TextField()


class Annotation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    integer = models.IntegerField(default=0)
    annotation = models.TextField(validators=[
        RegexValidator(
            regex='^[()\'aA-àÀ?âÂ, bB.cC; çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ]+$',
            message='All the characters should belong to character set "[()\'aA-àÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ]" ',
            code='invalid_characterset'
        ),
        RegexValidator(
            regex='(^[A-Z][\sa-z0-9]+$)|(^([A-Z]\w*\s*)+$)',
            message='Capital Letters are allowed only as first word letter or only if all letters in word are uppercase',
            code='invalid_capitalisation'
        ),
        RegexValidator(
            regex='(^\S+((\s\S+)+)$)|((^\S+((\s\S+)+))+\s$)',
            message='Only one space is allowed between the two characters',
            code='invalid_spaces'
        ),
        RegexValidator(
            regex='^.+([,;:]|\s)$',
            message='Characters ?.! should be end of text or followed by one space and an uppercase character and Characters ,;: should be end of text of followed by one space',
            code='invalid_characters'
        )
    ])
