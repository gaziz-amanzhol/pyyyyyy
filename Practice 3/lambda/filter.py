numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

numbers = [1, 2, -3, 4, 5, -6, 7, -8]
pos_numbers= list(filter(lambda x: x>0, numbers))
print(pos_numbers)

numbers = [1, 2, -3, 4, 5, -6, 7, -8]
neg_numbers= list(filter(lambda x: x<0, numbers))
print(neg_numbers)
