## Made by Zion Coding Incorporated

list1 = []
while True:
 option = input("Enter or View?: ").strip().capitalize()
 if option == "Enter":
    t = input("Enter item name: ")
    list1.append(t)
 elif option == "View":
    option2 = input("Use order number to view (O) or view entire list (L)?: ").strip().capitalize()
    if option2 == "O":
        ordernumber = int(input("Which item do you want to see (number)?: "))
        ordernumber -=1
        view = list1[ordernumber]
        print (view)
    elif option2 == "L":
        print (list1)
    else:
       print ("Invalid option.")
       continue
 else:
    print ("Invalid option.")
    continue
