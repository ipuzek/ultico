fajl = open("grupe_python.txt", encoding="utf8")
tekst = fajl.readlines()

print(fajl)

print(tekst)
tekst

for imePrezime in tekst:
    print(imePrezime)

inputFile = open("grupe_python.txt", encoding="utf8")
exportFile = open("grupe_python_DONE.txt", mode = "w", encoding="utf8")
for line in inputFile:
   new_line = line.replace('\t', ' ')
   exportFile.write(new_line) 

inputFile.close()
exportFile.close()

