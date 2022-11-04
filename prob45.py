import torch

Tn = 285
Pn = 2
Hn = 2
def Tri(n):
	return n*(n+1)/2
def Pent(n):
	return n*(3*n-1)/2
def Hexa(n):
	return n*(2*n-1)
T = Tri(Tn)
P = Pent(Pn)
H = Hexa(Hn)

while not (T == P and P == H):
	Tn += 1
	T = Tri(Tn)
	
	while P < T:
		Pn += 1
		P = Pent(Pn)
	while H < T:
		Hn += 1
		H = Hexa(Hn)

	if Tn % 100 == 0:
		print(Tn)

print(Tn, Pn, Hn, T, P, H)