def multiplication (n) :
# This function receives a number 'n'
# and returns another function.
# The returned function will multiply
# any number by 'n'.

    def multiply (x):
    # This inner function receives a number 'x'
    # and multiplies it by 'n', which comes from
    # the outer function.

        return x * n

    # Return the inner function
    return multiply

triplo = multiplication(3)
# Here we create a new function called 'triplo'
# 'multiplication(3)' means that 'n' is equal to 3
# So 'triplo' will multiply any number by 3

valor = triplo(5)
# Now we call the function 'triplo' with the value 5
# This means: 5 * 3

print(valor)
# Print the result on the screen