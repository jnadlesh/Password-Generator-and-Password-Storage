import pwgen

psw = ""
username = ""

def add():
    psw = ""
    username = input("Input your username: ")
    rngenpw = input("Do you want a random generated password (y/n): ").lower()
    if rngenpw == "y":
        psw = pwgen.generate()
    elif rngenpw == "n":
        psw = input("Input your password: ")
    else:
        print("Error: 0")
        quit()

    app = input("What is this for: ")
    f = open("secret.txt", "a")
    f.write(f"App: {app} | Username: {username} | Password: {psw}\n")
    f.close()

def view():
    f = open("secret.txt", "r")
    print(f.read().rstrip())
    f.close()

while True:
    inp = input("Would you like to (add/view) passwords or quit (q): ").lower()
    if inp == "q":
        break
    if inp == "add":
        add()
    elif inp == "view":
        view()
    else:
        continue

