# להוסיף למילון
def add():
    key = input("enter your URL:")
    value = input("enter your IP:")
    if key in dict:
        print("this name is exist")
    else:
        dict.update({key: value})
    print(dict)


#######################################################################################
# למחוק מהמילון


def remov():
    name = input("What URL you want to delete: ")
    del dict[name]
    print(dict)


########################################################################################
# לעדכן את המילון


def update():
    update1 = input("What url you want to update? : ")
    dict[update1] = input("enter hare: ")
    print(dict)


##################################################################################
# להדפיס בצורה יפה
def nice_print():
    for i in dict:
        print(i)


#########################################################################################
# חיפוש במילון
def searching():
    se = input("What URL you want to know if it exists? : ")
    print(se in dict)


#######################################################################################################################


dict = {}
for i in range(0, 1):
    name = input("enter your URL:")
    num = input("enter your IP:")
    if name in dict:
        print("this name is exist")
    else:
        dict.update({name: num})
print(dict)
choice = 0
while choice != "q":
    choice = input("\n1.If you want to add url and ip\n2.If you want to delete url and ip\n3.If you want to update "
                   "ip\n4.Print the dictionary nicely\n5.Search URL\n\nChoose one option: ")
    if choice == "1":
        add()
    elif choice == "2":
        remov()
    elif choice == "3":
        update()
    elif choice == "4":
        nice_print()
    elif choice == "5":
        searching()
    elif choice == "q":
        print("\nbey bey")
        break
    else:
        print("only 1-5 and q for exit\n")
