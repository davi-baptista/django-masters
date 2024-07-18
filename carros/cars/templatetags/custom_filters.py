from django import template

register = template.Library()

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

@register.filter
def format_currency_locale(value):
    return locale.format_string('%.2f', value, grouping=True)