import repository
from bson import ObjectId
def insertUser():
    name = input("Insira um nome: ")
    age = input("Insira uma idade: ")
    sector = input("sertor: ")
    langs = input("Insira suas linguagens(Separadas por espaço): ").split()
    exps = input("Insira o tempo de experiencia com cada linguagem: (Meses) ").split()
    langsDocArray = []
    for i in range(len(langs)):
        lang ={
            "name":langs[i],
            "experienceMonths":exps[i]
        }
        langsDocArray.append(lang)
    
    repository.user.insert_one({"name":name,"age":age,"sector":sector,"langs":langsDocArray})
    print("Documento inserido com sucesso!")


def findAll():
    if( empity()):
        raise ValueError("A colecao esta vazia!")

    else:
        print("Usuarios atuais:")
        for u in repository.user.find():
            print(u)
    print(" ") 
    print(" ")  

def filterBySectorName(sector):
    if empity():
       raise ValueError("A colecao esta vazia!")
    query = {"sector":sector}    
    collection = list( repository.user.find(query))
    if len ( collection) == 0:
      raise ValueError("Item nao encontrado")
    print("Usuarios do setor = ",sector)
    for u in collection:
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

def updateUser(newUser,id):
      documentId = ObjectId(id)
      filter = {"_id":documentId}
      langsDocArray = []

      for i in range(len(newUser.get("langs"))):
        lang ={
            "name":newUser.get("langs")[i],
            "experienceMonths":newUser.get("exps")[i]
        }
        langsDocArray.append(lang)

      newData = {"$set": {"name": newUser.get("name"), "age": newUser.get("age"),"sector":newUser.get("sector"),"langs":langsDocArray}}
      repository.user.update_one(filter,newData)



def deleteById(id):
      if empity():
        raise ValueError("A colecao esta vazia!")
      filter = {"_id":ObjectId(id)}
      
      repository.user.delete_one(filter)
      


def empity():
  return repository.user.count_documents({}) < 1