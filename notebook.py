notebook_list = list()
first_entry=int(input("Enter your first value in the list: "))
second_entry=int(input("Enter your second value in the list: "))
notebook_list.append(first_entry)
notebook_list.append(second_entry)

# for i in range(5):
#     val=(int(input("enter a value ")))
#     arr.append(val)
#     print (arr)

choise = input("If you want to add an entry press 1, If you want to delete an entry press 2, If you want to update an entry press 3 ")

def addition(entry): 
     notebook_list.append(entry) 
     return print(notebook_list)

def removal(entry_index):
    notebook_list.remove(notebook_list[entry_index])
    return print(notebook_list)

def update(val_old, val_new, notebook_list):
     for item in range(0, len(notebook_list)):
          if notebook_list[item] == val_old:
               notebook_list[item] == val_new
     print(notebook_list)

if choise == "1":    
     new_entry=(int(input("Enter the entry you wish to add")))
     addition(new_entry)

elif choise == "2":
     entry_index=(int(input("Which entry number do you want to delete. NOTE: 0 is the first element")))
     removal(entry_index)

elif choise == "3":
    val_old = int(input("Type the entry you want to change!"))
    val_new = int(input("What do you want to change it with?"))
    update(val_new,val_new,notebook_list)
