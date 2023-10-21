from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
   'en': '￥',
   'usd': '$',
   'rub': 'p'
}


@register.filter()
def currency(value, code='en'):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
   postfix = CURRENCIES_SYMBOLS[code]

   return f'{value} {postfix}'


