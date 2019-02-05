def addition (a,b):
    return a + b

def substraction (a,b):
    return a - b

def multiplication (a,b):
    return a * b

def division (a,b):
    return a / b   

arr = list()
for i in range(5):
    val=int (input("Enter a number:"))
    arr.append(val)
    print(arr)

choice = input("Enter p for sum, s for substraction, m for multiplication, d for division, 5 for sum and count ")
if choice == "p":
    print(arr[0], " + ", arr[1], " = ", addition(arr[0],arr[1]))
    
elif choice == "s":
    print(arr[0], " - ", arr[1], " = ", substraction(arr[0],arr[1]))
    
elif choice == "m":
    print(arr[0], " * ", arr[1], " = ", multiplication(arr[0],arr[1]))
    
elif choice == "d":
    print(arr[0], " / ", arr[1], " = ", division(arr[0],arr[1]))
    
elif choice == "5":
    print ("The sum and the count are: ", sum(arr)," , " , len(arr)  )
else:
        print ("Oops, try again")