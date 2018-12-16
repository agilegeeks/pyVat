import re
import math
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


        if vat_number[:2] != '10':
            return False

        checknum = int(vat_number[8])

        a1 = self.sum_weights([3, 7, 1, 3, 7, 1, 3, 7], vat_number)
        a2 = math.ceil(a1 / 10) * 10
        c9 = a2 - a1

        return checknum == c9
