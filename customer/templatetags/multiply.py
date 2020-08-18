from django import template         #multiply tag is user define tag
register = template.Library()

@register.simple_tag()
def multiply(price, qty):
    return price*qty