A = [[2,3,1],[4,7,3],[6,18,5]] 
b=[1,3,5]
n=len(A)
L = [[0,0,0], [0,0,0],[0,0,0]]
U= [[0,0,0],[0,0,0],[0,0,0]]

def dispmatrice(matrice):
    chaine = ""
    for i in matrice:
        for j in i:
            chaine+= f" {int(j)} "
        chaine+="\n"
    print(chaine)

#Décomposition LU
for i in range(n):
    print("Matrice U:")
    for j in range(i,n):
        print(f"->Position {i}-{j}")
        dispmatrice(U)
        U[i][j]=A[i][j] -sum(L[i][k]*U[k][j] for k in range(i))
    L[i][i]=1.0
    dispmatrice(U)
    print("Matrice L:")
    for j in range(i+1,n):
        print(f"->Position {i}-{j}")
        dispmatrice(L)
        L[j][i]=(A[j][i]-sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]

print(f"{L} \n {U}")
dispmatrice(L)

#Substitution avant, résolution de Ly=b
y= [0.0]*n
for i in range(n):
    somme = 0
    for j in range(i):
        somme+= L[i][j]*y[j]
    y[i]=(b[i]-somme)/L[i][i]
print(y)

#Substitution arrière, résolution de Ux=y
x = [0.0] * n
for i in range(n-1, -1, -1):
    somme = 0
    for j in range(i+1, n):
        somme += U[i][j] * x[j]
    x[i] = (y[i] - somme) / U[i][i]
print(x)

#Vérification du résultat, consiste à multiplier A par x et à retrouver b si tout fonctionne
résultat = []
for ligne in A:
    somme =0
    xcounter=0
    for colonne in ligne:
        somme+= colonne*x[xcounter]
        xcounter+=1
    résultat.append(somme)
print(résultat)