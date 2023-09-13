"""
Напишите функцию декоратор, которая переводит значение декорируемой функции
в рублях, в доллары (курс: 1$ = 72 рубля) или в евро (курс: 1€ = 80 руб).
Для тех, кто хочет добавить знак валюты:
chr(36) -> '$'
chr(8364) -> '€'
chr(8381) -> '₽'
"""
def decorator_currency(func):
    def wrapper(*args, **kwargs):
        rur = float(func(*args, **kwargs).strip(chr(8381)))
        usd_curs = 72
        eur_curs = 80
        print(f'In stock ruble: {rur} {chr(8381)}')
        print(f'Exchange rates: USD = {usd_curs} , EUR = {eur_curs}')
        can_buy_usd = f'{str(round(rur / usd_curs, 2))}'
        can_buy_eur = f'{str(round(rur / eur_curs, 2))}'
        return f"Can buy usd: {can_buy_usd} {chr(36)}\nCan buy euro: {can_buy_eur} {chr(8364)}"
    return wrapper
@decorator_currency
def summa(count: float, price: float) -> str:
    return f'{round(count * price, 2)}₽'


print(summa(35, 13))
