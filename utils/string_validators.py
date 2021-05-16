import re


def nip_validator(value: str) -> str or tuple:

    result = re.sub("-", "", re.findall(r"[\d{9}\-]*", value)[0])
    if len(result) == 10:
        return result
    return "Błąd NIP", f"Wartość {result} jest nieprawidłowa."


def bank_account_validator(value: str) -> str or tuple:

    result = "".join(re.findall(r"\d+", value))
    if len(result) == 26:
        return result
    return "Błąd rachunku bankowego", f"Wartość {result} jest nieprawidłowa"


def zip_code_validator(value: str) -> str or tuple:
    try:
        return re.sub("-", "", re.findall(r"\d{2}-?\d{3}", value.strip())[0])
    except IndexError:
        return (
            "Błąd kodu pocztowego",
            f"Wartość {value} jest nieprawidłowa dla pola: kod pocztowy",
        )
