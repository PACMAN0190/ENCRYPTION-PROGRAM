# 🔐 Python Substitution Cipher

This project is a simple encryption tool written in Python.  
It uses a **random substitution cipher** to transform text into an encrypted version based on a shuffled character key.

## 🚀 How It Works
1. A list of characters is created including:
   - uppercase and lowercase letters
   - digits
   - punctuation
   - space
2. The character list is shuffled to create a random encryption key.
3. Each character in the input text is replaced using the shuffled mapping.

## ▶️ Usage

Run the script:

```bash
python cipher.py

Then enter the text you want to encrypt when prompted.

🧠 Example

Input:

Hello World!

Output:

encrypted message : x9#P...
original message : Hello World!
⚠️ Note

Because the key is randomly generated each time, encrypted text cannot be decrypted unless the same key is saved.

📁 Requirements

Python 3.x

No external libraries required
