import random

my_list2 = []
for i in range(0, 6):
    number = random.randint(1, 37)
    while number in my_list2:
        number = random.randint(1, 37)
    my_list2.append(number)
print(my_list2)

list_user = []
while True:
    try:
        money = int(input("enter how money you have: "))
    except:
        print("is not int")
    else:
        x = money // 3
        break
i = 0
while i != x:
    ball = []
    for k in range(6):
        l = random.randint(1, 37)
        while l in ball:
            l = random.randint(1, 37)
        ball.append(l)
        ball.sort()
    if ball in list_user:
        continue
    else:
        i += 1
        # print(i)
        list_user.append(ball)
        list_user.sort()
print(list_user)

print(len(list_user))

list_counter = list()
for i in range((len(list_user))):
    counter = 0
    for g in range(len(list_user[i])):
        for k in range(len(my_list2)):
            if my_list2[k] == list_user[i][g]:
                counter += 1
    list_counter.append(counter)

print(list_counter)

pras = 0
for i in range(len(list_counter)):
    if list_counter[i] == 3:
        pras += 10
    elif list_counter[i] == 4:
        pras += 250
    elif list_counter[i] == 5:
        pras += 500
    elif list_counter[i] == 6:
        pras += 1000000
print("\nyou can win in " + str(pras))
