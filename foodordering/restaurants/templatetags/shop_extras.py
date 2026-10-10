from django import template

register = template.Library()


@register.filter
def get(dictionary, key):
    """{{ qtys|get:item.id }} -> the number stored under that key, or 0."""
    return dictionary.get(key, 0)
