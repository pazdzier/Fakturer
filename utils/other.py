import doctest
from decimal import Decimal

def perc_amounts_collector(bill) -> dict:
    """ """
    result = {}
    for service in bill.services:
        if service.service.percentage in result:
            result[service.service.percentage] += round(service.full_amount, 2)
        else:
            result[service.service.percentage] = round(service.full_amount, 2)
    return result


def all_percs_dict(values_lst: list):
    """
    >>> values_lst = [{'17%': Decimal('666.00')}, {'3%': Decimal('1234.66')}, {'17%': Decimal('2450.00')}]
    >>> result = x(values_lst)
    >>> result
    {'17%': Decimal('3116.00'), '3%': Decimal('1234.66')}
    """
    
    result = {}
    for val in values_lst:
        for key in val:
            if key in result:
                result[key] += round(val[key], 2)
            else:
                result[key] = round(val[key], 2)
    return result
    
if __name__ == '__main__':
    doctest.testmod()
