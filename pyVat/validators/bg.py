# Copyright 2018 Agile Geeks

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
# is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import (
    unicode_literals,
    print_function,
    division
)
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
            checksum = int(vat_number[8])
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

            return checksum == r

        # physical person
        checksum = int(vat_number[9])
        weights = [2, 4, 8, 5, 10, 9, 7, 3, 6]
        a1 = self.sum_weights(weights, vat_number[:9])
        r1 = a1 % 11
        if r1 == 10:
            r = 0
        else:
            r = r1
        if checksum == r:
            return True

        # foreigners
        checksum = int(vat_number[9])
        weights = [21, 19, 17, 13, 11, 9, 7, 3, 1]
        a1 = self.sum_weights(weights, vat_number[:9])
        r = a1 % 10
        if checksum == r:
            return True

        # others
        checksum = int(vat_number[9])
        weights = [4, 3, 2, 7, 6, 5, 4, 3, 2]
        a1 = self.sum_weights(weights, vat_number[:9])
        r1 = 11 - a1 % 11
        if r1 == 11:
            r = 0
        elif r1 == 10:
            return False
        else:
            r = r1
        if checksum == r:
            return True

        return False
