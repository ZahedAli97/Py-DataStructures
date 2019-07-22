# def maxi(n):
#     maximum = max(n)
#     maxind = n.index(maximum)
#     mini = n[0]
#     for i in range(0, maxind):
#         if n[i] < mini and i < maxind:
#             mini = n[i]
#             minind = i
#     return (maxind-minind)


def maxi(n):
    maxi = 0
    maxind = 0
    mini = 0
    minind = 0
    for i in range(len(n)):
        for j in range(i):
            if n[i]-n[j] > maxind-minind:
                maxi = n[i]
                maxind = i
                mini = n[j]
                minind = j
    print(maxi, "->", maxind, "  ", mini, "->", minind)
    return (maxind-minind)


# def newmaxi(n):
#     if n[0] > n[1]:
#         n[0], n[1] = n[1], n[0]
#     if n[0] < n[1]:
#         maxelem = n[1]
#         maxind = 1
#         minelem = n[0]
#         minind = 0
#     for indices in range(1, len(n)):
#         if n[indices] > maxelem:
#             print("From maxi", n[indices], indices, end=",")
#             maxelem = n[indices]
#             maxind = indices
#         if n[indices] < minelem:
#             print("From mini", n[indices], indices, end=",")
#             tempind = indices
#             if tempind > minind and tempind < maxind:
#                 minelem = n[indices]
#                 minind = indices
#     return (maxind-minind)


n = [14, 16, 7, 8, 19, 3, 4, 25, 7, 18, 9, 27, 18, 19, 25]
print(maxi(n))
# print(newmaxi(n))
