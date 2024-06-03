file = open(r"your file path",'r')
compactcode = ""
for line in file.readlines() :
    compactcode += line.strip()
print(compactcode)
