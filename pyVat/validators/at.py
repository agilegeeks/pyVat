import re
from .generic import GenericValidator


class Validator(GenericValidator):
    """
    For rules see /docs/VIES-VAT Validation Routines-v15.0.doc
    """
    def __init__(self):
        self.regexp = re.compile(r'^U\d{8}$', re.IGNORECASE)

    def validate(self, vat_number):
        if super(Validator, self).validate(vat_number) is False:
            return False

        vat_number = str(vat_number)

        checknum = int (vat_number[8])

        r = 0
        for i in range(3,8,2):
            digit = int (vat_number[i-1])
            r = r + ( int( digit/5 ) + (digit*2)%10 )

        c = 4
        for i in range(2,9,2):
            c = c + int (vat_number[i-1])

        c9 = (10 - (r+c)%10) % 10

        return checknum == c9
