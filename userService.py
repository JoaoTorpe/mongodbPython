import repository

def insertUser():
    name = input("Insira um nome: ")
    age = input("Insira uma idade: ")
    langs = input("Insira suas linguagens(Separadas por espaço): ").split()
    
    repository.user.insert_one({"name":name,"age":age,"programing languages":langs})
    print("Documento inserido com sucesso!")


def findAll():
    if( empity()):
        raise ValueError("A colecao esta vazia!")

    else:
        print("Usuarios atuais:")
        return repository.user.find()

def findByName(name):
  if empity():
        print("A coleção esta vazia!")
        return
  query = {"name":name}    
  collection = list( repository.user.find(query))
  if len ( collection) == 0:
      raise ValueError("Item nao encontrado")
  return collection

def empity():
  return repository.user.count_documents({}) < 1