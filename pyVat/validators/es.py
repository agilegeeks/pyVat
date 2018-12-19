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
        checksum = vat_number[8].upper()

        try:
            int( vat_number[8] )
        except:
            c9_is_number = False
        else:
            c9_is_number = True

        try:
            int( vat_number[0] )
        except:
            c1_is_number = False
        else:
            c1_is_number = True

        c1 = vat_number[0].upper()
        if c9_is_number:
            if c1 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'U', 'V']:
                return False
        else:
            if c1 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K',
                          'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'W', 'X', 'Y', 'Z' ]:
                return False

        # Juridical entities other than national ones
        if c9_is_number is False and c1 in ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                                            'H', 'N', 'P', 'Q', 'R', 'S', 'W']:
            s1 = int(vat_number[2]) + int(vat_number[4]) + int(vat_number[6])
            s2 = 0
            for i in range(1,8,2):
                digit = int(vat_number[i])
                s2 = s2 + int(digit/5) + (2 * digit) % 10
            r = 10 - (s1 + s2) % 10
            last_digit_mapping = {
                1: 'A',
                2: 'B',
                3: 'C',
                4: 'D',
                5: 'E',
                6: 'F',
                7: 'G',
                8: 'H',
                9: 'I',
                10: 'J'
            }
            if checksum == last_digit_mapping[r]:
                return True

        # # Physical persons
        if c9_is_number is False:
            if c1 in ['K', 'L', 'M', 'X', 'Y', 'Z'] or c1_is_number:
                new_c1 = c1
                if new_c1 == 'Y':
                    new_c1 = 1
                if new_c1 == 'Z':
                    new_c1 = 2
                new_vat_number = str(new_c1) + vat_number[1:]

                try:
                    int(new_c1)
                except:
                    new_c1_is_number = False
                else:
                    new_c1_is_number = True

                if new_c1_is_number:
                    r = sum(int(i) for i in new_vat_number[:8]) %23 + 1
                else:
                    r = sum(int(i) for i in new_vat_number[1:8]) % 23 + 1
                last_digit_mapping = {
                    1: 'T',
                    2: 'R',
                    3: 'W',
                    4: 'A',
                    5: 'G',
                    6: 'M',
                    7: 'Y',
                    8: 'F',
                    9: 'P',
                    10: 'D',
                    11: 'X',
                    12: 'B',
                    13: 'N',
                    14: 'J',
                    15: 'Z',
                    16: 'S',
                    17: 'Q',
                    18: 'V',
                    19: 'H',
                    20: 'L',
                    21: 'C',
                    22: 'K',
                    23: 'E'
                }
                if checksum == last_digit_mapping[r]:
                    return True

        if c9_is_number:
            checksum = int(vat_number[8])
            s1 = int(vat_number[2]) + int(vat_number[4]) + int(vat_number[6])
            s2 = 0
            for i in range(1, 8, 2):
                digit = int(vat_number[i])
                s2 = s2 + int(digit / 5) + (2 * digit) % 10
            r = 10 - (s1 + s2) % 10

            return checksum == (r % 10)

        return False



