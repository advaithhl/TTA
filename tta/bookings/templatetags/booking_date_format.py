# Credits to aumo's answer at https://stackoverflow.com/a/33106384
from django import template


register = template.Library()


@register.filter
def duration(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    if minutes:
        return f'{hours} hours {minutes} min'
    else:
        return f'{hours} hours'
