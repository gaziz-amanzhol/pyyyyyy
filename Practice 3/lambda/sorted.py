players = [("Messi", 38), ("Suarez", 39), ("Neymar", 34)]
sorted_players = sorted(players, key=lambda x: x[1])
print(sorted_players)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

numbers=[1,2,3,4,9,0,1]
sorted_numbers=sorted(numbers,key=lambda x: abs(x))
print(sorted_numbers)
