while True:
    a = (input("enter ip : "))
    s = a.split(".")
    print(s)
    if len(s) == 4:
        for i in range(4):
            if '1' > s[i] > '254':
                print("no good")
                break
            else:
                continue
        print("the ip " + str(a) + " is good")
    else:
        print("no good")
        
