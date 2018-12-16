import re
from .generic import GenericValidator


class Validator(GenericValidator):
    """
    For rules see /docs/VIES-VAT Validation Routines-v15.0.doc
    """
    def __init__(self):
        self.regexp = re.compile(r'^\d{8}$')

    def validate(self, vat_number):
        if super(Validator, self).validate(vat_number) is False:
            return False

        vat_number = str(vat_number)


        if vat_number[0] == '0':
            return False


        r = self.sum_weights([2, 7, 6, 5, 4, 3, 2, 1], vat_number)
        if r % 11 == 0:
            return True

        return False
