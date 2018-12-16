#from pyVat.validators.ro import Validator
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

    def test_de(self):
        validator = Validator('DE111111125')
        self.assertTrue(validator.validate())
        self.assertEqual(validator.country_code, 'DE')
        self.assertEqual(validator.vat_number, '111111125')

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

if __name__ == '__main__':
    unittest.main()

#
#
#
# validator = Validator()
#
# print (validator.validate(36804251))
