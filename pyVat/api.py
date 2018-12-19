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


VAT_NUMBER_REGEXPS = {
    'AT': re.compile(r'^U\d{8}$', re.IGNORECASE),
    'BE': re.compile(r'^\d{9,10}$'),
    'BG': re.compile(r'^\d{9,10}$'),
    'CY': re.compile(r'^\d{8}[a-z]$', re.IGNORECASE),
    'CZ': re.compile(r'^\d{8,10}$'),
    'DE': re.compile(r'^\d{9}$'),
    'DK': re.compile(r'^\d{8}$'),
    'EE': re.compile(r'^\d{9}$'),
    'ES': re.compile(r'^[\da-z]\d{7}[\da-z]$', re.IGNORECASE),
    'FI': re.compile(r'^\d{8}$'),
    'FR': re.compile(r'^[\da-z]{2}\d{9}$', re.IGNORECASE),
    'GB': re.compile(r'^((\d{9})|(\d{12})|(GD\d{3})|(HA\d{3}))$',
                     re.IGNORECASE),
    'GR': re.compile(r'^\d{9}$'),
    'HR': re.compile(r'^\d{11}$'),
    'HU': re.compile(r'^\d{8}$'),
    'IE': re.compile(r'^((\d{7}[a-z])|(\d[a-z]\d{5}[a-z])|(\d{6,7}[a-z]{2}))$',
                     re.IGNORECASE),
    'IT': re.compile(r'^\d{11}$'),
    'LT': re.compile(r'^((\d{9})|(\d{12}))$'),
    'LU': re.compile(r'^\d{8}$'),
    'LV': re.compile(r'^\d{11}$'),
    'MT': re.compile(r'^\d{8}$'),
    'NL': re.compile(r'^\d{9}B\d{2,3}$', re.IGNORECASE),
    'PL': re.compile(r'^\d{10}$'),
    'PT': re.compile(r'^\d{9}$'),
    'RO': re.compile(r'^\d{2,10}$'),
    'SE': re.compile(r'^\d{12}$'),
    'SI': re.compile(r'^\d{8}$'),
    'SK': re.compile(r'^\d{10}$'),
}

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

        if vat_country_code not in VAT_NUMBER_REGEXPS.keys():
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
