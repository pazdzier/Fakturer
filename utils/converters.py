import re
from datetime import date
from num2words import num2words


def numtoword(value: float) -> str:

    whole, frac = re.findall(r"\d+", str(value))
    num = num2words(whole, lang="pl")
    if whole == "1":
        zl = "złoty"
    elif whole in ["2", "3", "4"]:
        zl = "złote"
    else:
        zl = "złotych"
    if frac == "01":
        gr = "grosz"
    elif frac in ["02", "03", "04"]:
        gr = "grosze"
    else:
        gr = "groszy"
    frac = num2words(frac, lang="pl")
    return f"{num} {zl} {frac} {gr}"


def bill_name(bills_count: int):

    month_year = date.today().strftime("%m/%Y")
    return f"RACHUNEK nr {bills_count + 1}/{month_year}"


def bill_file_name(bill_name):

    return re.sub('/', ' ', bill_name)
