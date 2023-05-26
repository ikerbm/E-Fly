from django import template

register = template.Library()

@register.filter
def to_letter(number):
    if isinstance(number, int):
        return chr(ord('A') + number - 1)
    return number

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def divide(value, arg):
    return int(value / arg)

