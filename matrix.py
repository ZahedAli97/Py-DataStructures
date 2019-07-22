m = [[1, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0]]
n = m
for i in m:
    for j in i:
        print(j, end=" ")
    print("")


def scanrow(row):
    c = 0
    for i in m[row]:
        if i == 1:
            c += 1
    if c == 0:
        return True
    else:
        return False


def scancol(col):
    c = 0
    for i in range(len(m)):
        # for j in m[i][col]:
        if m[i][col] == 1:
            c += 1
    if c == 0:
        return True
    else:
        return False


sr = []
sc = []
print("--rows:")
for i in range(len(m)):
    # print(scanrow(i))
    sr.append(scanrow(i))

print("--cols:")
for i in range(len(m[0])):
    # print(scancol(i))
    sc.append(scancol(i))

count = 0
for i in m:
    #sr = scanrow(count)
    for j in range(len(i)):
        #sc = scancol(j)
        # srv = sr[count]
        # scv = sc[j]
        # print(srv, scv)
        if sr[count] == True and sc[j] == True:
            # print("Hi", count, j)
            n[count][j] = 0
        else:
            n[count][j] = 1

        # if m[count][j] == 1:
        #     temp = j
        #     for k in range(len(m)):
        #         n[k][temp] = 1
        #         n[count][k] = 1
        #     # m[j][count] = 1
    count += 1


print("New Matrix")
for i in n:
    for j in i:
        print(j, end=" ")
    print("")
