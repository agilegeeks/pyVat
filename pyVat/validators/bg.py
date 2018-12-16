import re
from .generic import GenericValidator


class Validator(GenericValidator):
    """
    For rules see /docs/VIES-VAT Validation Routines-v15.0.doc
    """

    def __init__(self):
        self.regexp = re.compile(r'^\d{9,10}$')

    def validate(self, vat_number):
        if super(Validator, self).validate(vat_number) is False:
            return False

        vat_number = str(vat_number)

        # if is legal entity
        if (len(vat_number)==9):
            checknum = int(vat_number[8])
            a1 = self.sum_weights(list(range(1,9)), vat_number[:8])
            r1 = a1 % 11

            if r1 == 10:
                a2 = self.sum_weights(list(range(3,11)), vat_number[:8])
                r2 = a2 % 11
                if r2 == 10:
                    r = 0
                else:
                    r = r2
            else:
                r = r1

            return checknum == r

        # physical person
        checknum = int(vat_number[9])
        weights = [2, 4, 8, 5, 10, 9, 7, 3, 6]
        a1 = self.sum_weights(weights, vat_number[:9])
        r1 = a1 % 11
        if r1 == 10:
            r = 0
        else:
            r = r1
        if checknum == r:
            return True

        # foreigners
        checknum = int(vat_number[9])
        weights = [21, 19, 17, 13, 11, 9, 7, 3, 1]
        a1 = self.sum_weights(weights, vat_number[:9])
        r = a1 % 10
        if checknum == r:
            return True

        # others
        checknum = int(vat_number[9])
        weights = [4, 3, 2, 7, 6, 5, 4, 3, 2]
        a1 = self.sum_weights(weights, vat_number[:9])
        r1 = 11 - a1 % 11
        if r1 == 11:
            r = 0
        elif r1 == 10:
            return False
        else:
            r = r1
        if checknum == r:
            return True

        return False


