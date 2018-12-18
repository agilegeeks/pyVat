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
import sys
from .generic import GenericValidator

PY_3_OR_HIGHER = sys.version_info >= (3, 0)

class Validator(GenericValidator):
    """
    For rules see /docs/VIES-VAT Validation Routines-v15.0.doc
    """
    ccm = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
        16: 'G',
        17: 'H',
        18: 'J',
        19: 'K',
        20: 'L',
        21: 'M',
        22: 'N',
        23: 'P',
        24: 'Q',
        25: 'R',
        26: 'S',
        27: 'T',
        28: 'U',
        29: 'V',
        30: 'W',
        31: 'X',
        32: 'Y',
        33: 'Z'

    }

    def __init__(self):
        self.regexp = re.compile(r'^[\da-z]{2}\d{9}$', re.IGNORECASE)

    def validate(self, vat_number):
        if super(Validator, self).validate(vat_number) is False:
            return False

        vat_number = str(vat_number)

        try:
            int(vat_number)
        except:
            new_style = True
        else:
            new_style = False

        if new_style is False:
            checkval = int(vat_number[2:] + '12') % 97
            return int(vat_number[:2]) == checkval
        else:
            if PY_3_OR_HIGHER:
                inv_ccm = {v: k for k, v in Validator.ccm.items()}
            else:
                inv_ccm = {v: k for k, v in Validator.ccm.iteritems()}

            s1 = inv_ccm[vat_number[0]]
            s2 = inv_ccm[vat_number[1]]

            try:
                c1 = int(vat_number[0])
            except:
                s = s1 * 34 + s2 - 100
            else:
                s = s1 * 24 + s2 - 10

            p = s / 11 + 1
            r1 = s % 11
            r2 = int(vat_number[2:]) % 11

            return r1 == r2


