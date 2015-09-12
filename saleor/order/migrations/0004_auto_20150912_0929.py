# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20150825_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverygroup',
            name='shipping_price',
            field=django_prices.models.PriceField(decimal_places=4, verbose_name='shipping price', default=0, editable=False, currency='EUR', max_digits=12),
        ),
    ]
