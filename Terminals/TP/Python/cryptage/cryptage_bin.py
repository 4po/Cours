#ou exclusif a et b sont des booleens
def oue (a,b):
	if(a != b):
		return 1
	else:
		return 0

def Crypte(Mess,Clef):
	Mcrypte = []
	for i in range(len(Mess)):
		Mcrypte.append(oue(Mess[i],Clef[i]))
	return Mcrypte


M = [0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,0]

K = [1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,1]

C = Crypte(M,K)
D = Crypte(C,K)

print(M)
print(C)
print(D)
