
PLACEHOLDER = "[name]"


with open("letterformat/names/name.txt", mode="r") as names:
    namelist = names.readlines()
    print(namelist)

with open("letterformat/letter.txt") as letter:
    content = letter.read()

    for names in namelist:
        stripname = names.strip()
        new_letter = content.replace(PLACEHOLDER, stripname)
        with open(f"sendlist/letter_for_{stripname}", mode="w") as sendlist:
            sendlist.write(new_letter)
