import userService

def display():
    print("1 - Inserir usuario")
    print("2 - Listar todos os usuarios")
    print ("3 - Listar todos filtrados por nome")
    print("5 - Sair")
    return input("--->>>>")


value = 0

while value != 5:
    value = int( display())

    match value:
        case 1:
          userService.insertUser()
          
    