import re
import math
import calendar
import datetime
from .generic import GenericValidator


class Validator(GenericValidator):
    """
    For rules see /docs/VIES-VAT Validation Routines-v15.0.doc
    """

    def __init__(self):
        self.regexp = re.compile(r'^\d{8,10}$')

    def validate(self, vat_number):
        if super(Validator, self).validate(vat_number) is False:
            return False

        vat_number = str(vat_number)

        # legal entities
        if len(vat_number) == 8:
            if vat_number[0] == '9':
                return False
            checknum = int (vat_number[7])
            a1 = self.sum_weights(list(range(8,1,-1)), vat_number[:8])
            if a1 % 11 == 0:
                a2 = a1 + 11
            else:
                a2 = math.ceil(a1/11) * 11
            c8 = (a2 - a1) % 10

            return checknum == c8

        # individuals
        if len(vat_number) == 9:

            # special cases
            if vat_number[0] == '6':
                checknum = int(vat_number[8])
                a1 = self.sum_weights(list(range(8, 1, -1)), vat_number[1:8])
                if a1 % 11 == 0:
                    a2 = a1 + 11
                else:
                    a2 = math.ceil(a1/11) * 11
                d = a2 - a1
                last_digit_mapping = {
                    1: 8,
                    2: 7,
                    3: 6,
                    4: 5,
                    5: 4,
                    6: 3,
                    7: 2,
                    8: 1,
                    9: 0,
                    10: 9,
                    11: 8
                }
                return checknum == last_digit_mapping[d]
            else:
                # common individuals
                if int(vat_number[:2])>53:
                    return False

                monthval = int(vat_number[2:4])
                if monthval not in range (1,13) and monthval not in range(51,63):
                    return False

                if monthval>12:
                    monthval = monthval - 50
                num_days_month = calendar.monthrange( int('19'.join(vat_number[:2])), monthval)[1]

                daysval = int(vat_number[4:6])
                if daysval<1 or daysval>num_days_month:
                    return False

                return True

        # individuals - born between 1954 and 1999
        if len(vat_number) == 10:
            if int(vat_number) % 11 != 0:
                return False

            current_year = str(datetime.date.today().year)
            current_year = int(current_year[2:])
            yearval = int(vat_number[:2])
            if yearval not in range (current_year+1) and yearval not in range(54,100):
                return False

            monthval = int(vat_number[2:4])
            if monthval not in range(1, 13) and monthval not in range(21, 33)\
                    and monthval not in range(51, 63) and monthval not in range(71, 83):
                return False

            year_prefix = '19'
            if yearval<13:
                year_prefix = '20'
            num_days_month = calendar.monthrange(int(year_prefix.join(vat_number[:2])), monthval)[1]
            daysval = int(vat_number[4:6])
            if daysval < 1 or daysval > num_days_month:
                return False

            a1 = 0
            for i in range(0,9,2):
                a1 = a1 + int(vat_number[i] + vat_number[i+1])

            if a1 % 11 != 0:
                return False

            return True

        return False
