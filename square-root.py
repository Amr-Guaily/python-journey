# Find a square root for any number (int or float numbers)

# question: what is the square root of 2?
# answer: 1.4142135623730951. so we need to thik about the concept of approximation
# We will use binary search technique

x = float(input("Enter a number: "))
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low) / 2.0

while abs(ans ** 2 - x) >= epsilon and ans <= x:
    print("low = " + str(low) + " high = " + str(high) + " ans = " + str(ans))
    numGuesses += 1
    
    if ans ** 2 < x:
        low  = ans
    else:
        high = ans

    ans = (high + low) / 2.0

print("numGuesses = " + str(numGuesses))
print(str(ans) + " is close to the square root of " + str(x))
