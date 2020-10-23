from django import template
from django.utils.encoding import force_text

register = template.Library()


@register.filter
def intdot(val_orig):
    val_text = force_text(val_orig)
    val_new = val_text.replace(',', '.')
    return val_new
