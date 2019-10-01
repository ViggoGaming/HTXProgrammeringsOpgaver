"""
a) Skriv et program, der generer multiplikationstabellen for 2 fra 2 til og med 20 og gem
tabellen i en liste: [2, 4, 6, 8, 10, 12, ..., 20].
b) Udvid programmet, så 20 kan specificeres af brugeren.
c) Udvid programmet, så brugeren kan få multiplikationstabellen for et vilkårligt naturligt tal x.
d) Udvid programmet, så det udskriver multiplikationstabellerne fra 2 til og med x.
"""

"""
x=5

2: 2 4 6 ...
3: 3 6 9 ...
4: 4 8 12 ...
5: 5 10 15 ...
"""

x = int(input("x="))

for i in range(2, x+1):
	print("{}: {}".format(str(i), ", ".join(list(map(str, [num*i for num in range(1, 10+1)])))))