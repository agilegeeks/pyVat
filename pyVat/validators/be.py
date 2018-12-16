import re
from .generic import GenericValidator


class Validator(GenericValidator):
    """
    For rules see /docs/VIES-VAT Validation Routines-v15.0.doc
    """
    def __init__(self):
        self.regexp = re.compile(r'^0[1-9]{1}\d{8}$')

    def validate(self, vat_number):
        if super(Validator, self).validate(vat_number) is False:
            return False

        vat_number = str(vat_number)

        checknum = int(vat_number[8:10])
        checkval = 97 - ( int(vat_number[:8]) % 97 )

        return checkval == checknum
