import re

class GenericValidator(object):
    """
    Generic validator
    """

    def __init__(self):
        self.regexp = re.compile(r'^.{1,}$')

    def validate(self, vat_number):
        vat_number = str(vat_number)
        if not self.regexp.match(vat_number):
            return False


    def sum_weights(self, weights, number, start_pos=0):
        checkval = 0;
        for i in range(start_pos, len(weights)):
            checkval = checkval + int(number[i]) * weights[i]
        return checkval