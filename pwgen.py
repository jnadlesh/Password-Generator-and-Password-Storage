import randomElement as rnd
list_of_characters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "X", "x", "Y", "y", "Z", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@", "#", "$", "%", "^", "&", "*", "!"]

def generate():
    password = []
    i = 0
    while i <= 25:
        index = rnd.randomElement(list_of_characters)
        password.append(index)

        i += 1

    final_password = "".join(password)
    return final_password




def pgenerate():
    password = []
    i = 0
    while i <= 25:
        index = rnd.randomElement(list_of_characters)
        password.append(index)

        i += 1

    final_password = "".join(password)
    print(final_password)

a = 0
while a <= 1:
    pgenerate() 
    a += 1