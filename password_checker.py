import string

# List of common weak passwords
common_passwords = [
    "123456",
    "password",
    "password123",
    "admin",
    "admin123",
    "qwerty",
    "abc123"
]

# Get password from user
password = input("Enter your password: ")

# Check if password is common
if password.lower() in common_passwords:
    print("\nPassword Strength: WEAK")
    print("Reason: This is a commonly used password.")
    exit()

# Initialize counters
length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_symbol = False

# Check each character
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in string.punctuation:
        has_symbol = True

# Calculate score
score = 0

if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1

# Display password details
print("\nPassword Analysis")
print("---------------------------")
print("Length:", length)
print("Contains Uppercase:", has_upper)
print("Contains Lowercase:", has_lower)
print("Contains Number:", has_digit)
print("Contains Symbol:", has_symbol)

# Decide password strength
print("\nPassword Strength:", end=" ")

if score <= 2:
    print("WEAK")
elif score == 3 or score == 4:
    print("MEDIUM")
else:
    print("STRONG")