#Tian and Aaron

def decode(password):
    password = list(password)
    for element in range(len(password)):
        password[element] = (int(password[element]) - 3)
        if password[element] < 0:
            password[element] = 10 + password[element]
    password = ''.join(map(str, password))
    return password

