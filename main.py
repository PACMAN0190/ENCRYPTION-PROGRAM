import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
print(f"chars : {chars}")
print(f"key : {key}")
cipher_text = input("Enter a text to encrypt : ")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]


print(f"encrypted message : {plain_text}")
print(f"original message : {cipher_text}")
