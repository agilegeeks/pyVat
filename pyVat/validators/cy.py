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
        self.regexp = re.compile(r'^\d{8}[a-z]$', re.IGNORECASE)

    def validate(self, vat_number):
        if super(Validator, self).validate(vat_number) is False:
            return False

        vat_number = str(vat_number)
        if int(vat_number[0]) not in [0, 1, 3, 4, 5, 9]:
            return False
        if vat_number[:2] == str('12'):
            return False

        odd_digit_mapping = {
            0: 1,
            1: 0,
            2: 5,
            3: 7,
            4: 9,
            5: 13,
            6: 15,
            7: 17,
            8: 19,
            9: 21
        }
        a1 = 0
        for i in range(8):
            if i % 2 == 0:
                a1 = a1 + odd_digit_mapping [ int(vat_number[i]) ]
            else:
                a1 = a1 + + int(vat_number[i])

        r = a1 % 26

        last_char_mapping = {
            0: 'A',
            1: 'B',
            2: 'C',
            3: 'D',
            4: 'E',
            5: 'F',
            6: 'G',
            7: 'H',
            8: 'I',
            9: 'J',
            10: 'K',
            11: 'L',
            12: 'M',
            13: 'N',
            14: 'O',
            15: 'P',
            16: 'Q',
            17: 'R',
            18: 'S',
            19: 'T',
            20: 'U',
            21: 'V',
            22: 'W',
            23: 'X',
            24: 'Y',
            25: 'Z'
        }

        last_char = vat_number[8]
        last_char = last_char.upper()

        return last_char_mapping[r] == last_char
