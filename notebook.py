arr = list()
for i in range(5):
    val=(int(input("enter a value ")))
    arr.append(val)
    print (arr)

choise = input("If you want to add an entry press 1, If you want to delete an entry press 2, If you want to update an entry press 3 ")

def addition(valadd): 
     arr.append(valadd) 
     return print(arr)

def removal(valindex):
    arr.remove(arr[valindex])
    return print(arr)

def update(valchange, valnew, arr):
     for item in range(0, len(arr)):
          if arr[item] == valchange:
               arr[item] == valnew
     print(arr)

if choise == "1":    
     valadd=(int(input("What do you want to add?")))
     addition(valadd)

elif choise == "2":
     valindex=(int(input("Which entry number do you want to delete from 0 to 4. NOTE: 0 is the first element")))
     removal(valindex)

elif choise == "3":
    valchange = int(input("Type the entry you want to change!"))
    valnew = int(input("What do you want to change it with?"))
    update(valchange,valnew,arr)
