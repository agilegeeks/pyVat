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
        validator = Validator('GB263321723')
        self.assertTrue(validator.validate())
        validator = Validator('GB151699094')
        self.assertTrue(validator.validate())


    def test_hr(self):
        validator = Validator('HR99999999999')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'HR')
        validator = Validator('HR9999999999')
        self.assertFalse(validator.validate())

    def test_hu(self):
        # format 1 - 5 chars
        validator = Validator('HU21376414')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'HU')
        validator = Validator('hu 10597190')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'HU')


    def test_ie(self):
        # old style format
        validator = Validator('IE8Z49289F')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'IE')
        validator = Validator('IE26287395')
        self.assertFalse(validator.validate())

        # new style
        validator = Validator('IE3628739L')
        self.assertTrue(validator.validate())

    def test_it(self):
        validator = Validator('IT00000010215')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'IT')
        validator = Validator('IT00000017775')
        self.assertFalse(validator.validate())

    def test_lt(self):
        # juridical entities
        validator = Validator('LT213179412')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'LT')
        validator = Validator('LT213179422')
        self.assertFalse(validator.validate())

        # Temporarily registered taxpayers
        validator = Validator('LT290061371314')
        self.assertTrue(validator.validate())
        validator = Validator('LT290061371324')
        self.assertFalse(validator.validate())

    def test_lu(self):
        validator = Validator('LU10000356')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'LU')
        validator = Validator('LU14516304')
        self.assertTrue(validator.validate())
        validator = Validator('LU10000355')
        self.assertFalse(validator.validate())

    def test_lv(self):
        # juridical entities
        validator = Validator('LV40003009497')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'LV')
        validator = Validator('LV40003009498')
        self.assertFalse(validator.validate())

        # natural persons
        validator = Validator('LV07091910933')
        self.assertTrue(validator.validate())
        validator = Validator('LV32091910933')
        self.assertFalse(validator.validate())

    def test_mt(self):
        validator = Validator('MT15121333')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'MT')
        validator = Validator('MT15121332')
        self.assertFalse(validator.validate())

    def test_nl(self):
        validator = Validator('NL010000446B01')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'NL')
        validator = Validator('NL000000446B01')
        self.assertFalse(validator.validate())

    def test_pl(self):
        validator = Validator('PL5260001246')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'PL')
        validator = Validator('PL5260001244')
        self.assertFalse(validator.validate())

    def test_pt(self):
        validator = Validator('PT502757191')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'PT')
        validator = Validator('PT502757190')
        self.assertFalse(validator.validate())

    def test_ro(self):
        validator = Validator('RO2785503')
        self.assertTrue( validator.validate() )
        self.assertEqual( validator.country_code, 'RO' )
        self.assertEqual( validator.vat_number, '2785503' )
        validator = Validator('2785503', 'RO')
        self.assertTrue(validator.validate())

        validator = Validator('ro 99 908')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'RO')

        validator = Validator('RO2785500')
        self.assertFalse(validator.validate())

    def test_se(self):
        validator = Validator('SE556188840401')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'SE')
        validator = Validator('SE556183840407')
        self.assertFalse(validator.validate())

    def test_si(self):
        validator = Validator('SI15012557')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'SI')
        validator = Validator('SI15012556')
        self.assertFalse(validator.validate())

    def test_sk(self):
        validator = Validator('SK4030000007')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'SK')
        validator = Validator('SK5407062531')
        self.assertFalse(validator.validate())
        validator = Validator('SK0407062531')
        self.assertFalse(validator.validate())


suite = unittest.TestLoader().loadTestsFromTestCase(TestValidator)
unittest.TextTestRunner(verbosity=2).run(suite)
