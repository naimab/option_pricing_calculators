# Project Name

Option Pricing Calculators

## Features

bsm.py: Uses the Black-Scholes model to calculate the value of a European option.
binom.py: Uses the binomial method to calculate the value of an American option

## Limitations

The binomial method in binom.py does not account for dividends. However, it offers an efficient calculation method due to its creative use of sparse matrices.

## Usage

To use either of the option pricing calculators, simply import the necessary functions from the respective file:

from bsm import function_name_here
from binom import another_function_name_here

For detailed information on each function and its parameters, please refer to the docstrings within the respective .py files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
