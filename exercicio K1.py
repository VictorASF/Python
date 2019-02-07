l1 = [4, 5, 1, 8]
l2 = ['b', 'n', 'e', 't']

print(l1)
print(l2)
l3 = l1+l2
print(l3)
print('Item com indice 5 = {} '.format(l3[5]))
for idx, item in enumerate(l3):
    print(idx,'<=>', item)