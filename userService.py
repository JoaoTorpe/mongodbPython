import repository
from bson import ObjectId
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
        for u in repository.user.find():
            print(u)
    print(" ")        

def findByName(name):
  if empity():
       raise ValueError("A colecao esta vazia!")
  query = {"name":name}    
  collection = list( repository.user.find(query))
  if len ( collection) == 0:
      raise ValueError("Item nao encontrado")
  print("Usuarios que possuem nome = ",name)
  for u in collection:
      print(u)
  print(" ")  

def deleteById(id):
      if empity():
        raise ValueError("A colecao esta vazia!")
      filter = {"_id":ObjectId(id)}
      
      repository.user.delete_one(filter)
      


def empity():
  return repository.user.count_documents({}) < 1