def random_elem(lista, n=1):
    length = len(lista)
    indices = set()
    if n > length:
        n = length
    while len(indices) < n:
        index = hash(tuple(indices)) % length
        indices.add(index)
    return [lista[index] for index in indices]




fruits = ["apple", "banana", "orange", "kiwi", "grape"]

random_fruit = random_elem(fruits,4)
print(random_fruit)  # Véletlenszerűen kiválasztott gyümölcs (pl.: "banana")


