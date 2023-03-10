# Python program to convert a real value
# to IEEE 754 Floating Point Representation.

# Function to convert a fraction to binary form.
def binaryOfFraction(fraction):
    binary = str()

    # Iterating through fraction until it becomes Zero.
    while (fraction):
        fraction *= 2 # Multiplying fraction by 2.

        # Storing Integer Part of fraction in int_part.
        if (fraction >= 1):
            int_part = 1
            fraction -= 1
        else:
            int_part = 0

        # Adding int_part to binary after every iteration.
        binary += str(int_part)

    # Returning the binary string.
    return binary


# Function to get sign bit, exp bits and mantissa bits from given real no.
def floatingPoint(real_no):
    sign_bit = 0

    if (real_no < 0):
        sign_bit = 1

    # converting given no. to absolute value as we have
    # already set the sign bit.
    real_no = abs(real_no)

    # Converting Integer Part of Real no to Binary
    int_str = bin(int(real_no))[2:]

    # Function call to convert fraction part of real no to Binary.
    fraction_str = binaryOfFraction(real_no - int(real_no))

    # Getting the index where bit was high for the first
    # Time in binary repres of Integer part of real no.
    ind = int_str.index('1')

    # The Exponent is the no. by which we have right
    # Shifted the decimal and it is given below.
    # Also converting it to bias exp by adding 127.
    exp_str = bin((len(int_str) - ind - 1) + 127)[2:]

    # getting mantissa string by adding int_str and fraction_str.
    # the zeroes in MSB of int_str have no significance so they
    # are ignored by slicing.
    mant_str = int_str[ind + 1:] + fraction_str

    # Adding Zeroes in LSB of mantissa string so as to make it's length of 23 bits.
    mant_str = mant_str + ('0' * (23 - len(mant_str)))

    return sign_bit, exp_str, mant_str

# Example
sign_bit, exp_str, mant_str = floatingPoint(-2.25)

# Final Floating point Representation.
ieee_32 = str(sign_bit) + '|' + exp_str + '|' + mant_str

# Printing the ieee 32 representation.
print("IEEE 754 representation of -2.250000 is :")
print(ieee_32)

aa = binaryOfFraction(1.75)
print(aa)
