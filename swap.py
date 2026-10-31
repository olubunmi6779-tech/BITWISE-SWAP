
# BITWISE SWAP CHALLENGE

# STEP 1: Swap Without a Third Variable
print("STEP 1: SWAP WITHOUT A THIRD VARIABLE")

a = 15
b = 25

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)


# STEP 2: Perform XOR Swap
print("\nSTEP 2: XOR SWAP")

x = 10
y = 20

print("Before swapping:")
print("x =", x)
print("y =", y)

x = x ^ y
y = x ^ y
x = x ^ y

print("After swapping:")
print("x =", x)
print("y =", y)


# STEP 3: Use Left Shift to Double Numbers
print("\nSTEP 3: LEFT SHIFT")

number = 5

print("Original number:", number)
print("Left shift by 1:", number << 1)
print("Left shift by 2:", number << 2)
print("Left shift by 3:", number << 3)


# STEP 4: Detect Different Signs with XOR
print("\nSTEP 4: SIGN DETECTION")

num1 = -15
num2 = 20

if (num1 < 0) ^ (num2 < 0):
    print("The numbers have different signs.")
else:
    print("The numbers have the same sign.")


# STEP 5: Divide Without Using /
print("\nSTEP 5: DIVISION USING REPEATED SUBTRACTION")

dividend = 23
divisor = 5

if divisor == 0:
    print("Error: Division by zero is not allowed.")
else:
    quotient = 0
    remainder = dividend

    while remainder >= divisor:
        remainder = remainder - divisor
        quotient = quotient + 1

    print("Dividend:", dividend)
    print("Divisor:", divisor)
    print("Quotient:", quotient)
    print("Remainder:", remainder)


# STEP 6: Program Completed
print("\nBITWISE SWAP CHALLENGE COMPLETED!")
