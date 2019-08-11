from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    value_time = datetime.fromtimestamp(value)
    diff_time = datetime.now() - value_time
    ten_minutes = 600
    one_day = 24*60*60

    if diff_time.seconds <= ten_minutes:
        value = 'Только что'
    elif diff_time.seconds <= one_day:
        hours_ago = int(diff_time.seconds / 3600)
        value = f'{hours_ago} часов назад'
    else:
        value = value_time.strftime('%Y-%m-%d')

    return value

@register.filter
def format_score(value):
    if value < -5:
        return 'Все плохо'
    elif value > 5:
        return 'Хорошо'
    else:
        return 'Нейтрально'

@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    elif value > 50:
        return '50+'
    return value

@register.filter
def format_selftext(value, count):
    if value:
        text = value.split()
        if text > count*2:
            text = text[:count] + ['...'] + text[-count:]
            text = ' '.join(text)
            return text
        else:
            return text
    return ''



