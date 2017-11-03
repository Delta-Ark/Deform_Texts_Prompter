load_text = raw_input("filename: ")
f = open(load_text)

text = []
for line in f:
    text.append(line)

loop = 1
while loop == 1:

    replace_this = raw_input("replace this: ")
    with_this = raw_input("with this: ")

    for idx, line in enumerate(text):
        text[idx] = line.replace(replace_this, with_this)
        print text[idx]

    if replace_this == "  ":
        loop = 2
