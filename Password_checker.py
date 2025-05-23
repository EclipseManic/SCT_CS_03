# Importing the 're' module for using regular expressions (pattern matching)
import re

# Define a function named 'checker' that takes a password as input
def checker(password):
    # Score will track how many rules the password satisfies (out of 5)
    score = 0

    # List of rules to validate the password
    # Each rule is a tuple: (pattern, message_if_failed, message_if_passed)
    rules = [
        (r".{8,}", "❌ Password must contain 8 characters\n", "✅ You have fulfilled the criteria of minimum 8 length\n"),
        (r"[A-Z]", "❌ Password must contain a Capital Alphabet\n", "✅ You have fulfilled the criteria of a Capital Alphabet\n"),
        (r"[a-z]", "❌ Password must contain a Small Alphabet\n", "✅ You have fulfilled the criteria of a Small Alphabet\n"),
        (r"[!@#$%^&*()_+={}:;\"'<>?,./\\]", "❌ Password must contain a Special Character\n", "✅ You have fulfilled the criteria of a Special Character\n"),
        (r"[0-9]", "❌ Password must contain a Number\n", "✅ You have fulfilled the criteria of a Number\n")
    ]

    # Loop through each pattern rule
    for pattern, wrong, right in rules:
        # Check if the pattern exists in the password (valid)
        if re.search(pattern, password):
            print(right)  # Print the success message
            score += 1    # Increase score by 1
        # If the pattern is NOT found (invalid)
        if not re.search(pattern, password):
            print(wrong)  # Print the error message

    # Show overall password strength based on the score
    if score == 5:
        print("🤩🤩💫 Your password has strong strength.\n")
    elif 3 <= score < 5:
        print("🤧😶 Your password is good, but could be stronger.\n")
    else:
        print("🤮🤢🤕 Your password is weak.\n")

# Take password input from the user
password = input("Enter the password :- ")

# Call the checker function with the input password
checker(password)
