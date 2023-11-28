# Find the cube root of a perfect cube

# Question: what's kind of algorithm this is !!?
# Answer: This an example of Guess&Check and it's called "exhaustive enumeration"
# Exhaustive enumeration is a silly technique (takes a lot of gusses). we refer to such algorithms as brute force algorithm that searches all possible

x = int (input("Enter a integer: "))

# While loop version
# ans = 0
# while ans * ans * ans  < abs(x):
#     ans = ans + 1
#     print ("current guess = " + str(ans))

# if ans * ans * ans != abs(x):
#     print (str(x) + " Is not a perfect cube")
# else:
#     if x < 0:
#         ans = -ans
#     print ("Cube root of " + str(x) + " is " + str(ans))

# For loop version
for ans in range(abs( x + 1)):
    print ("current guess = " + str(ans))
    if ans ** 3 == abs(x):
        break

if ans ** 3 != abs(x):
    print (str(x) + " Is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print ("Cube root of " + str(x) + " is " + str(ans))
