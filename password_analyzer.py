
import re
import getpass

COMMON_PASSWORDS = {
    "password", "password123", "123456",
    "12345678", "qwerty", "admin",
    "admin123", "welcome", "letmein"
}

def analyze_password(password):
    checks = {
        "Length >= 12": len(password) >= 12,
        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Number": bool(re.search(r"[0-9]", password)),
        "Special character": bool(re.search(r"[^A-Za-z0-9]", password))
    }

    score = sum(checks.values())
    suggestions = []

    for rule, passed in checks.items():
        if not passed:
            suggestions.append("Improve: " + rule)

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append("Avoid common passwords")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


password = getpass.getpass("Enter password: ")
strength, suggestions = analyze_password(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("All basic checks passed!")
