from django import template

register = template.Library()

@register.filter
def to_letter(number):
    if isinstance(number, int):
        return chr(ord('A') + number - 1)
    return number

@register.filter
def get_clase(clase):
    if(clase == 'primera') : return 'Primera Clase'
    else: return 'Clase Económica'

@register.filter
def get_precio(clase, vuelo):
    if(clase == 'primera') : return vuelo.precioPrimera
    else: return vuelo.precioEconomica


@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def substract(value, arg):
    return value - arg

@register.filter
def divide(value, arg):
    return int(value / arg)

