from django import template
import random

register = template.Library()

DESCRIPTIONS = [
    'Sunglasses enthusiast',
    'Aggressive typer',
    'Politics nerd',
    'Chart animator'
]

@register.simple_tag
def rand_description():
    return random.choice(DESCRIPTIONS)