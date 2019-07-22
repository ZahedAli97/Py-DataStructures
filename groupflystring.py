msg = "Hello how are you how do you do"
msglist = msg.split()
print(msglist)

for i in msglist:
    # print(type(i))
    for j in i:
        count = i.count(j)
        if count > 1:
            if i in msglist:
                msglist.remove(i)

for i in msglist:
    print(i, end=" ")
print()
