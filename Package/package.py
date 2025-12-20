filename="file.txt"
with open(filename,"w") as f:
    f.write("My Name is Ronish, ")
    f.write("I love singing")

print(f'filename {filename} is created and added the content')

with open(filename,"r") as f:
    c=f.read()
print(c)

with open(filename,"a") as f:
    f.write("Appending ")
