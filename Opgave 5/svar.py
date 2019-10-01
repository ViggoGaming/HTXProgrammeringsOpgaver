"""
Formel:
Lix = O / P + L * 100 / O

O = Antal ord i teksten = word_amount
P = Antal punktummer = period_amount
L = Antal lange ord(> 6) = long_word_amount

a) 
Lav et program, der bestemmer Lix-tallet af en tekststreng. Programmet skal fortælle
hvilket niveau teksten ligger på. Antag at du får teksten i en string-variable.

b) 
Benyt din LIX-beregner på en tekst du skrev i folkeskolen og en tekst, du har skrevet i
gymnasiet (det kunne f.eks. være en dansk stil).
"""

text = open("input.txt", 'r').read()

words = text.split()
word_amount = len(words)
period_amount = text.count('.')
long_word_amount = 0

for word in words:
	if len(word) > 6:
		long_word_amount += 1

LIX = round((word_amount/period_amount)+((long_word_amount*100)/word_amount), 2)

print(f"words: {word_amount}")
print(f"periods: {period_amount}")
print(f"long words: {long_word_amount}\n")
print(f"LIX = {LIX}")