numbers2 = [6, -5, 3, -8, 4, -2, 5, -4, 11]

for v in numbers2:
    if v < 0:
        numbers2.insert(0,v)

print("new numbers2 =", numbers2)