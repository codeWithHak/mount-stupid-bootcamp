# 🧠 Day 4 Challenge: “Password Strength Checker”

## You're building a tool that checks how strong a password is, based on a few simple rules.

### 💻 Requirements:
Ask the user for a password and tell them if it’s:


__❌ Weak__ – fewer than 6 characters or only letters

__⚠️ Medium__ – at least 6 characters, must include letters and numbers

__✅ Strong__ – at least 8 characters, must include letters, numbers, and special characters (!@#$%^&* etc.)

### 🧪 Example:

Enter password: hello
→ Weak

Enter password: hello123
→ Medium

Enter password: Hello@123
→ Strong

### ⚙️ Hints:
Use any(char.isdigit() for char in password)

Use any(char.isalpha() for char in password)

Check for special characters using string punctuation: string.punctuation

