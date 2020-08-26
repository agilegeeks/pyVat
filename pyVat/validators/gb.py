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
        self.regexp = re.compile(r'^((\d{9})|(\d{12})|(GD\d{3})|(HA\d{3}))$', re.IGNORECASE)

    def validate(self, vat_number):
        if super(Validator, self).validate(vat_number) is False:
            return False

        vat_number = str(vat_number)

        # Format 1
        if len(vat_number) == 5:
            ranges = {
                'GD': range(500),
                'HA': range(500,1000),
            }
            if int(vat_number[2:]) not in ranges[ vat_number[:2] ]:
                return False
            return True

        # Format 2
        c89 = int(vat_number[7:9])
        c17 = int(vat_number[:7])
        r = self.sum_weights(list(range(8, 1, -1)), vat_number[:7]) + c89
        r1 = r % 97
        r2 = (r + 55) % 97
        if (r1 * r2) != 0 or (r1 + r2) == 0:
            return False
        if r1 == 0:
            for rng in [range(100000, 1000000),
                            range(9490001, 9700001),
                            range(9990001, 10000000)]:
                if c17 in rng:
                    return False

        if r2 == 0:
            if c17 in range(1, 1000001):
                return False

        if len(vat_number) == 12:
            if int(vat_number[9:]) == 0:
                return False

        return True
