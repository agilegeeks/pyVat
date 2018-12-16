import re
import math
from .generic import GenericValidator


class Validator(GenericValidator):
    """
    For rules see /docs/VIES-VAT Validation Routines-v15.0.doc
    """
    def __init__(self):
        self.regexp = re.compile(r'^[\da-z]\d{7}[\da-z]$', re.IGNORECASE)

    def validate(self, vat_number):
        if super(Validator, self).validate(vat_number) is False:
            return False


        vat_number = str(vat_number)

        try:
            int( vat_number[8] )
        except:
            c9_is_number = False
        else:
            c9_is_number = True

        c1 = vat_number[0].upper()
        if c9_is_number:
            if c1 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'U', 'V']:
                return False
        else:
            if c1 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K',
                          'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'W', 'X', 'Y', 'Z' ]:
                return False


        # case A)
        if c9_is_number is False and c1 in ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                                            'H', 'N', 'P', 'Q', 'R', 'S', 'W']:
            s1 = int(vat_number[2]) + int(vat_number[4]) + int(vat_number[6])