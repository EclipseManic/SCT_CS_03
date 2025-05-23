## Password Strength Checker
Project Title: Password Strength Checker
Author: EclipseManic

## Description:
This Python script checks the strength of a password based on predefined criteria. It evaluates the password against multiple rules and provides feedback on its security level, along with tips for improvement.

## Features:
# Checks for the following password criteria:

Minimum length of 8 characters

At least one uppercase letter

At least one lowercase letter

At least one special character (e.g., !@#$%^&*())

At least one numeric digit

# Provides visual feedback (✅/❌) for each criterion.

Assigns a strength score:

Strong (5/5 criteria met)

Good (3-4 criteria met)

Weak (<3 criteria met)

Emoji-enhanced output for clarity.

## Requirements:

Python 3.x

Terminal/console that supports emojis (for proper display)

## Installation:

Clone the repository or download the script password_checker.py.

Ensure Python is installed on your system.

## Usage:

Run the script in your terminal:

bash
python password_checker.py
Enter a password when prompted.

## Example:

bash
Enter the password :- Pass123!
✅ You have fulfilled the Criateria of minimum 8 length
✅ You have fulfilled the Criateria of minimum a Capital Alphabet
✅ You have fulfilled the Criateria of minimum a Small Alphabets
✅ You have fulfilled the Criateria of minimum a special Character
✅ You have fulfilled the Criateria of minimum a Number Value
🤩🤩💫 You're password have a strong strength......
Output Explanation:

✅ Indicates a passed criterion.

❌ Indicates a failed criterion.

Final strength rating is displayed with emojis.

## Note:

The feedback messages reflect the exact criteria checked by the script (including typos like "Criateria" for "Criteria").

Ensure your terminal supports emojis to view the output correctly.

## Contributing:
Contributions are welcome! Open an issue or submit a pull request for improvements, bug fixes, or additional features.

License:
This project is licensed under the MIT License.

## Author:
EclipseManic
GitHub: https://github.com/EclipseManic

## Acknowledgments:
Built using Python's re module for regex pattern matching.
