frutas = ["maçã", "banana", "laranja"]


frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]


fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"


frutas.sort() # Ordena a lista em ordem alfabética
print(frutas)  # Imprime ["maçã", "pera", "uva"]

print(frutas)
frutas.reverse()    # Inverte a ordem da lista
print(frutas)  # Imprime ["uva", "pera", "maçã"]

