from django import template

register = template.Library()

@register.filter
def cell_color(value):
    if value == '-':
        color = '#FFFFFF'
    else:
        if float(value) < 0:
            color = '#008000'
        elif 1 <= float(value) <= 2:
            color = '#FCD3D3'
        elif 2 < float(value) <= 5:
            color = '#F98C8C'
        elif float(value) > 5:
            color = '#FF0000'
        else:
            color = '#FFFFFF'
    return color