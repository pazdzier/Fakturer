import re


def zip_code_format(value):
    try:
        return re.sub(r"(\d{2})(\d{3})", r"\1-\2", value)
    except TypeError:
        return value

def nip_format(value: str):
    try:
        return re.sub(r"(\d{3})(\d{2})(\d{2})(\d{3})", r"\1-\2-\3-\4", value)
    except TypeError:
        return value

def account_format(value: str):
    try:
        return re.sub(
            r"(\d{2})?(\d{4})?(\d{4})?(\d{4})?(\d{4})?(\d{4})?(\d{4})?",
            r"\1 \2 \3 \4 \5 \6 \7",
            value,
        )
    except TypeError:
        return value
