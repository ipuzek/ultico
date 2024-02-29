# turn on/off
# search bar => settings.json


print("hello")

# palindrom

word = input("Upiši potencijalni palindrom...")

if word == word[::-1]:
    print("PALINDROM")
else:
    print("nije palindrom")

def jest_palindrom(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
jest_palindrom("ana")
jest_palindrom("Ana")
jest_palindrom("AnA")

