"""
x = "This is the first Line\n"
y = "This is the second line\n"
z = "This is the third line"
line = [x, y, z]
with open("file.txt", "w") as f:
    for i in line:
        f.write(i)

"""
"""
lines = ["This is the line", "This is the second line", "this is the Third Line"]

with open("file.txt", "w") as fp:
    for line in lines:
        fp.write(line+"\n")


"""
"""

with open("file.txt", "r") as f:
    lines = f.readline()
    print(lines)
    for line in lines:
        print(line)
        
"""
"""
with open("file.txt", "r") as fp:
    for line in fp:
        print(line)

"""
"""
with open("file.txt", "r") as fp:
    print(fp.read())
"""
"""
with open("file.txt", "w") as fp:
    print(fp.read())
"""
