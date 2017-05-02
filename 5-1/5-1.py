# Ntcn d 23-55
# получить list из кубов всех чисел, делящихся и на 3, и на 4 без остатка, взятых из массива чисел mass
# Использовать List Comprehensions.
# В ответе написать код - одна строчка.

new_list = [x**3 for x in mass if x % 12 == 0]
print(new_list)


