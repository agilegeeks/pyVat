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

import unittest

from pyVat.api import Validator

class TestValidator(unittest.TestCase):

    def test_ro(self):
        validator = Validator('RO2785503')
        self.assertTrue( validator.validate() )
        self.assertEqual( validator.country_code, 'RO' )
        self.assertEqual( validator.vat_number, '2785503' )
        validator = Validator('2785503', 'RO')
        self.assertTrue(validator.validate())

        validator = Validator('ro 278  5503')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'RO')

        validator = Validator('RO2785500')
        self.assertFalse(validator.validate())

    def test_at(self):
        validator = Validator('ATU10223006')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'AT')

        validator = Validator('ATU10223005')
        self.assertFalse(validator.validate())

    def test_be(self):
        validator = Validator('BE0776091951')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'BE')
        self.assertEqual(validator.vat_number, '0776091951')

        validator = Validator('BE0776091950')
        self.assertFalse(validator.validate())

        validator = Validator('BE0842411247')
        self.assertTrue(validator.validate())

    def test_bg(self):

        # test legal entity
        validator = Validator('BG101004508')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'BG')
        self.assertEqual(validator.vat_number, '101004508')

        validator = Validator('BG101004502')
        self.assertFalse(validator.validate())

        # test physical person
        validator = Validator('BG0041010002')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'BG')
        self.assertEqual(validator.vat_number, '0041010002')

        # foreigners
        validator = Validator('BG0000100159')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'BG')
        self.assertEqual(validator.vat_number, '0000100159')

        # others
        validator = Validator('BG0000100153')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'BG')
        self.assertEqual(validator.vat_number, '0000100153')

        validator = Validator('BG202618588')
        self.assertTrue(validator.validate())

    def test_cy(self):
        validator = Validator('CY00532445O') # the last char is O from oranges
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'CY')
        self.assertEqual(validator.vat_number, '00532445O')

        validator = Validator('CY12000139V')
        self.assertFalse(validator.validate())


    def test_cz(self):

        # test legal entity
        validator = Validator('CZ46505334')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'CZ')
        self.assertEqual(validator.vat_number, '46505334')

        validator = Validator('CZ46505332')
        self.assertFalse(validator.validate())

        # test individuals - special cases
        validator = Validator('CZ640903926')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'CZ')
        self.assertEqual(validator.vat_number, '640903926')

        validator = Validator('CZ46505331')
        self.assertFalse(validator.validate())

        # test common individuals
        validator = Validator('CZ395601439')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'CZ')
        self.assertEqual(validator.vat_number, '395601439')
        validator = Validator('CZ520229439')
        self.assertTrue(validator.validate())

        validator = Validator('CZ705601439')
        self.assertFalse(validator.validate())

        # test common individuals born after 1953
        validator = Validator('CZ7103192745')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'CZ')
        self.assertEqual(validator.vat_number, '7103192745')

        validator = Validator('CZ7103192744')
        self.assertFalse(validator.validate())

        validator = Validator('CZ26159708')
        self.assertTrue(validator.validate())

    def test_de(self):
        validator = Validator('DE111111125')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'DE')
        self.assertEqual(validator.vat_number, '111111125')
        validator = Validator('DE124718735')
        self.assertTrue(validator.validate())
        validator = Validator('DE180295363')
        self.assertTrue(validator.validate())
        validator = Validator('DE123475223')
        self.assertTrue(validator.validate())

        validator = Validator('DE111111122')
        self.assertFalse(validator.validate())

    def test_dk(self):
        validator = Validator('DK88146328')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'DK')
        self.assertEqual(validator.vat_number, '88146328')

        validator = Validator('DK88146327')
        self.assertFalse(validator.validate())

    def test_ee(self):
        validator = Validator('EE100207415')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'EE')
        self.assertEqual(validator.vat_number, '100207415')

        validator = Validator('EE100207417')
        self.assertFalse(validator.validate())

    def test_gr(self):
        validator = Validator('EL040127797')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'GR')
        self.assertEqual(validator.vat_number, '040127797')
        validator = Validator('040127797', 'EL')
        self.assertTrue(validator.validate())

        validator = Validator('EL040127798')
        self.assertFalse(validator.validate())

        validator = Validator('EL999863881')
        self.assertTrue(validator.validate())

    def test_es(self):
        # Juridical entities other than national ones
        validator = Validator('esa0011012B')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'ES')
        self.assertEqual(validator.vat_number, 'A0011012B')
        validator = Validator('ESA0011012B')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'ES')
        self.assertEqual(validator.vat_number, 'A0011012B')
        validator = Validator('ESA0011012B', 'ES')
        self.assertTrue(validator.validate())

        validator = Validator('ESA0011011B')
        self.assertFalse(validator.validate())

        # Physical persons
        validator = Validator('ESZ3964521D')
        self.assertTrue(validator.validate())
        validator = Validator('ESM3964521F')
        self.assertTrue(validator.validate())

        # National juridical entities
        validator = Validator('ESB84968312')
        self.assertTrue(validator.validate())
        validator = Validator('ESB50860162')
        self.assertTrue(validator.validate())
        validator = Validator('ESB30034573')
        self.assertTrue(validator.validate())

    def test_fi(self):
        validator = Validator('fi09853608')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'FI')

        validator = Validator('FI09853607')
        self.assertFalse(validator.validate())

    def test_fr(self):
        # old style
        validator = Validator('FR00300076965')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'FR')
        validator = Validator('FR06300076967')
        self.assertTrue(validator.validate())
        validator = Validator('FR46441049376')
        self.assertTrue(validator.validate())
        validator = Validator('Fr28316607779')
        self.assertTrue(validator.validate())

        validator = Validator('FR00300076964')
        self.assertFalse(validator.validate())

        validator = Validator('FR2A316607779')
        self.assertTrue(validator.validate())

        #  new style
        validator = Validator('FR0K300076962')
        self.assertTrue(validator.validate())

    def test_gb(self):
        # format 1 - 5 chars
        validator = Validator('GbGD232')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'GB')
        validator = Validator('GBHA232')
        self.assertFalse(validator.validate())
        validator = Validator('GBGD755')
        self.assertFalse(validator.validate())
        self.assertEqual(validator.country_code, 'GB')
        validator = Validator('GBHA957')
        self.assertTrue(validator.validate())

        #format 2
        validator = Validator('GB434031494')
        self.assertTrue(validator.validate())

if __name__ == '__main__':
    unittest.main()

#
#
#
# validator = Validator()
#
# print (validator.validate(36804251))
