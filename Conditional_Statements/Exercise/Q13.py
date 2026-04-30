password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True

if len(password) < 8:
    print("Invalid")
elif has_upper and has_lower and has_digit:
    print("Strong")
else:
    print("Weak")