# Generated by Django 3.0.6 on 2020-05-30 11:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotatorbackend', '0007_auto_20200529_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='annotation',
            field=models.TextField(validators=[django.core.validators.RegexValidator(code='invalid_characterset', message='All the characters should belong to character set "[()\'aA-àÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ]" ', regex="^[()'aA-àÀ ? âÂ , bB . cC ; çÇ : dD !eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ]+$"), django.core.validators.RegexValidator(code='invalid_spaces', message='Only one space is allowed between the two characters', regex='^([\\S]+ [\\S]+)+\\s*$'), django.core.validators.RegexValidator(code='invalid_characters', message='Characters ?.! should be end of text or followed by one space and an uppercase character and Characters ,;: should be end of text of followed by one space', regex='(([?.!]|\\s[A-Z])$)|(([,;:]|\\s)$)')]),
        ),
    ]
