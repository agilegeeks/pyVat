# A library for checking on European VAT formats

[![Build Status](https://api.travis-ci.com/agilegeeks/pyVat.svg?branch=master)](https://travis-ci.com/agilegeeks/pyVat)

pyVat is a complete library that validates vat number formats in EU member countries. The algorithms used are described in /doc/VIES-VAT Validation Routines-v15.0.doc

## Compatibility
Python >= 2.6

## Installation
    $ pip install vat-format-checker

## Usage
```python
from pyVat.api import Validator
validator = Validator('ATU10223006')
if validator.validate() is True:
    print ("The VAT number has a valid format")
else:
    print ("Invalid VAT number format for country %s" % validator.country_code)

```
## Issues
- The Croatian format is missing the algorithm. The validations is done purely based on regular expressions.
