import doctest
import re
from datetime import date
from num2words import num2words


def numtoword(value: float) -> str:
    """
    >>> numtoword(7350.20)
    'siedem tysięcy trzysta pięćdziesiąt złotych dwadzieścia groszy'
    >>> numtoword(66.02)
    'sześćdziesiąt sześć złotych dwa grosze'
    >>> numtoword(50.01)
    'pięćdziesiąt złotych jeden grosz'
    >>> numtoword(666.66)
    'sześćset sześćdziesiąt sześć złotych sześćdziesiąt sześć groszy'
    >>> numtoword(2450.10)
    'dwa tysiące czterysta pięćdziesiąt złotych dziesięć groszy'
    >>> numtoword(50.50)
    'pięćdziesiąt złotych pięćdziesiąt groszy'
    >>> numtoword(50.44)
    'pięćdziesiąt złotych czterdzieści cztery grosze'
    """
    whole, frac = str(value).split('.')
    if len(frac) == 1:
        frac = frac + '0'
    num = num2words(whole, lang="pl")
    if whole == "1":
        zl = "złoty"
    elif whole in ["2", "3", "4"]:
        zl = "złote"
    else:
        zl = "złotych"
    if frac == "01":
        gr = "grosz"
    elif re.match('\d{1}[2,3,4]{1}', frac):
        gr = "grosze"
    else:
        gr = "groszy"
    frac = num2words(frac, lang="pl")
    return f"{num} {zl} {frac} {gr}"


def bill_name(bills_count: int):

    month_year = date.today().strftime("%m/%Y")
    return f"RACHUNEK nr {bills_count + 1}/{month_year}"


def bill_file_name(bill_name: str) -> str:
    """
    >>> bill_file_name("RACHUNEK nr 1/2022")
    'RACHUNEK nr 1 2022'
    """
    return re.sub('/', ' ', bill_name)


if __name__ == '__main__':
    doctest.testmod()
