import re
from .generic import GenericValidator


class Validator(GenericValidator):
    """
    For rules see /docs/VIES-VAT Validation Routines-v15.0.doc
    """

    def __init__(self):
        self.regexp = re.compile(r'^\d{2,10}$')

    def validate(self, vat_number):
        if super(Validator, self).validate(vat_number) is False:
            return False

        vat_number = str(vat_number)

        vat_number = vat_number.rjust(10,'0')
        checksum = int (vat_number[9])
        weights = [7, 5, 3, 2, 1, 7, 5, 3, 2]
        checkval = self.sum_weights(weights, vat_number)
        checkval = (checkval * 10) % 11
        if checkval==10:
            checkval=0
        return checkval == checksum