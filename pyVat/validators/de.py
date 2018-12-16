import re
from .generic import GenericValidator


class Validator(GenericValidator):
    """
    For rules see /docs/VIES-VAT Validation Routines-v15.0.doc
    """
    def __init__(self):
        self.regexp = re.compile(r'^\d{9}$')

    def validate(self, vat_number):
        if super(Validator, self).validate(vat_number) is False:
            return False

        vat_number = str(vat_number)

        checknum = int (vat_number[8])

        if vat_number[0] == '0':
            return False

        p = 10
        for i in range(8):
            s = int(vat_number[i]) + p
            m = s % 10
            if m == 0:
                m = 10
            p = (2 * m) % 11
        r = 11 - p
        if r == 10:
            c9 = 0
        else:
            c9 = r

        return checknum == c9
