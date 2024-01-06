import userService

def display():
    print("1 - Inserir usuario")
    print("2 - Listar todos os usuarios")
    print ("3 - Listar todos filtrados por nome")
    print("4 - Deletar usuario por ID")
    print("5 - Atualizar usuario")
    print("6 - Listar todos os setores")
    print("-1 - Sair")
    return input("--->>>> ")

value = 0

while value != -1:
    value = int(display())

    match value:
        case 1:
          userService.insertUser()
        case 2:
            try:
             userService.findAll()
            except ValueError as vl:
               print("Erro: ",vl)
        case 3:
            print(" ")
            try:
             userService.findByName(input("Insira um nome: "))
            except ValueError as vl:
               print("Erro: ",vl)
        case 4:           
             userService.deleteById(input("Insira o Id: "))
        case 5: 
             id = input("Id do usuario a ser atualizado: ")
             user = {
                "name":input("Novo nome: "),
                "age": input("Nova idade: "),
                "langs": input("Novas linguagens (separadas por espaco): ").split(),
                "exps" : input("Insira o tempo de experiencia com cada linguagem: (Meses) ").split()
             }
             userService.updateUser(user,id)    
        case 6:
             userService.findAllSectors()             
        case -1:
           print("Programa encerrado!")
        
        case _:
          print("Opcao invalida!")