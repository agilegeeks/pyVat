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

        checknum = int(vat_number[8])

        a1 = self.sum_weights([256, 128, 64, 32, 16, 8, 4, 2], vat_number)
        a2 = a1 % 11
        c9 = a2 % 10

        return checknum == c9
