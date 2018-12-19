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


EU_COUNTRIES = [
    'AT',
    'BE',
    'BG',
    'CY',
    'CZ',
    'DK',
    'EE',
    'FI',
    'FR',
    'DE',
    'GR',
    'HR',
    'HU',
    'IE',
    'IT',
    'LV',
    'LT',
    'LU',
    'MT',
    'NL',
    'PL',
    'PT',
    'RO',
    'SK',
    'SI',
    'ES',
    'SE',
    'GB'
]
def load_class(module_name, class_name):
    mod = __import__(module_name, fromlist=[class_name])
    klass = getattr(mod, class_name)
    return klass

def load_cc_validator(cc):
    module_name = 'pyVat.validators.%s' % cc
    klass_name = 'Validator'
    klass = load_class(module_name, klass_name)
    return klass

class VatValidationError(Exception):
    """
    Exception thrown by the Validator object when the VAT number is not valid
    """
    pass

class Validator(object):

    def __init__(self, vat_number, vat_country_code=None):

        self.error_message = None
        self.vat_number = vat_number
        self.vat_country_code = vat_country_code


    def clean(self):
        vat_number = self.vat_number
        vat_country_code = self.vat_country_code

        try:
            vat_number = str(vat_number)
        except:
            VatValidationError('Invalid VAT number provided')
        vat_number = vat_number.replace(' ', '')

        if vat_country_code is not None:
            try:
                vat_country_code = str(vat_country_code)
            except:
                VatValidationError('Invalid VAT country provided')
            vat_country_code = vat_country_code.replace(' ', '')
            vat_country_code = vat_country_code.upper()
        # if no vat_country_code provided we try to extract it from vat_number
        else:
            try:
                vat_country_code = vat_number[:2]
            except:
                raise VatValidationError('Invalid VAT number provided')

            vat_country_code = vat_country_code.upper()


            vat_number = vat_number[2:]

        if vat_country_code == 'EL':
            vat_country_code = 'GR'

        if vat_country_code not in EU_COUNTRIES:
            raise VatValidationError('Invalid VAT country')

        if len(vat_number)>2:
            if vat_number[:2].upper() == vat_country_code:
                vat_number = vat_number[2:]

        return vat_number.upper(),vat_country_code.upper()

    def validate(self):
        try:
            self.vat_number, self.country_code = self.clean()
        except VatValidationError as e:
            self.error_message = str(e)
            return False

        validator_klass = load_cc_validator(self.country_code.lower())
        validator = validator_klass()
        return validator.validate(str(self.vat_number))
