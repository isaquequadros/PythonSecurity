import itertools

string = input("string a ser permutada: ")

resultado = itertools.permutations(string, len(string))

for i in resultado:
	print(''.join(i))
