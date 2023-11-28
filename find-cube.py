# Find the cube root of a perfect cube
x = int (input("Enter a integer: "))
ans = 0

while ans * ans * ans  < abs(x):
    ans = ans + 1
    print ("current guess = " + str(ans))

if ans * ans * ans != abs(x):
    print (str(x) + " Is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print ("Cube root of " + str(x) + " is " + str(ans))