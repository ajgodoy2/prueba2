from django import template

register = template.Library()


@register.filter
def listify(value):
    if not value:
        return ""
    if len(value) == 1:
        return str(value[0])
    to_return = ""
    for i in range(1, len(value)):
        to_return += str(value[i - 1]) + ", "
    to_return += str(value[len(value) - 1])
    return to_return
