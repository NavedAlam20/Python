num = int(input("Enter number: "))

# Positive / Negative / Zero
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Even / Odd
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Multiple of 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("Multiple of both 3 and 5")