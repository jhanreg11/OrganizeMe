import bcrypt

def print_TODO():
    with open('data.txt', 'r') as file:
        data = file.read()
        tokens = data.split('\n')[2:]
        i = 1
        for x in tokens:
            if x != '':
                print(i, '. ', x)
                i += 1

def add_TODO():
    todo = input("Enter in the todo to add: ")
    with open('data.txt', 'a') as file:
        file.write(todo)
        file.write('\n')

def delete_TODO():
    to_be_deleted = input("Enter the indice of the todo to delete (-1 to show all todo's): ")
    if int(to_be_deleted) == -1:
        print_TODO()
        delete_TODO()
    msg = ''
    with open('data.txt', 'r') as file:
        tokens = file.read().split('\n')
        tokens = [x for x in tokens if x != '']
        try:
            msg = "Are you sure you want to delete \'" + tokens[int(to_be_deleted)+1] + "\' (y/n): "
        except IndexError:
            print("ERROR list index out of range.")
            delete_TODO()
    if input(msg) == 'y':
        with open('data.txt', 'w') as file:
            for x in tokens:
                if x != tokens[int(to_be_deleted)+1]:
                    file.write(x)
                    file.write('\n')

choice = input("Login (0) Create Account (1): ")

if int(choice) == 1:
    username = input("Create Username: ")
    password = input("Create Password: ")
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    with open('data.txt', 'w') as file:
        file.write(username)
        file.write('\n')
        file.write(hashed)
        file.write('\n')

if int(choice) == 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    data = ""

with open('data.txt', 'r') as file:
    data = file.read()
    tokens = data.split('\n')[:2]
    if tokens[0] == username:
        if bcrypt.checkpw(password.encode('utf-8'), tokens[1].encode('utf-8')):
            choice = input("View TODO's (0), Add TODO's (1), Check Off TODO (2), Log Out (3): ")
            while int(choice) != 3:
                if int(choice) == 0:
                    print_TODO()
                if int(choice) == 1:
                    add_TODO()
                if int(choice) == 2:
                    delete_TODO()
                choice = input("View TODO's (0), Add TODO's (1), Check Off TODO (2), Log Out (3): ")





