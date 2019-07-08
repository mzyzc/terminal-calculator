#!/usr/bin/env python

import sys

import operators as op

# Checks that both the function and operand(s) variables have been provided.
if len(sys.argv) < 2:
    print('Usage: [command] [operand] ...')
    sys.exit()
function = sys.argv[1]
operands = [float(x) for x in sys.argv[2:]]

# Establishes valid keywords for performing an operation.
addition_commands = ['sum', 'add', 'addition']
subtraction_commands = ['difference', 'subtract', 'subtraction']
multiplication_commands = ['product', 'multiply', 'multiplication']
division_commands = ['quotient', 'divide', 'division']

# Calculates the answer using the correct function.
if function in addition_commands:
    answer = op.sum_(operands)
elif function in subtraction_commands:
    answer = op.difference(operands)
elif function in multiplication_commands:
    answer = op.product(operands)
elif function in division_commands:
    answer = op.quotient(operands)

# Converts answer to integer, if applicable.
if answer == int(answer):
    answer = int(answer)
print(answer)