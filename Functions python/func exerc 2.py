def create_name(first, last):
    return first + " " + last


def create_name2(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("\nRafael", "Cruz\n")
full_name2 = create_name2("rafael", "andrade")

print(full_name)

print(full_name2)

