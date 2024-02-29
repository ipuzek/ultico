# lower() vs .lower()

U = input("Imaš li ušteđevine? Da/Ne ")
U.lower()
U
uu = U.lower()
uu
(U, uu) # tuple


if U.lower() == "da":
    USTD = int(input("molim te napiši dosadašnju ušteđevinu: "))
else:
    USTD = int(0)

print(USTD)

# A method is a function that belongs to a specific class. 
U.lower() # Thus lower is a function that belongs to a string class
