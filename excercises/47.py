import string

letters = string.ascii_lowercase
l = []
for i in letters:
    with open("letters/" + i + ".txt") as file:
        file_read = file.read()
        if file_read in 'python':
            l.append(file_read)

print(l)