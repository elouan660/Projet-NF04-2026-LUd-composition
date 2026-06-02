A = [[2,3,1],[4,7,3],[6,18,5]] # Matrice recherchée
b=[1,3,5]
n=len(A)
L = []
U= []

for i in range(n):
    tabU=[] #Deux tableaux temporaires différents pour éviter les problèmes d'adresse mémoire
    tabL=[]
    for j in range(n):
        tabU.append(0)
        tabL.append(0)
    L.append(tabL)
    U.append(tabU)


def dispmatrice(matrice):
    chaine = ""
    for i in matrice:
        for j in i:
            chaine+= f" {int(j)} "
        chaine+="\n"
    print(chaine)

def dispvecteur(vecteur):
    for coord in vecteur:
        print(coord)

#Décomposition LU, voir le l'algorithme papier pour le détail des formules
for i in range(n):
    print("Matrice U:")
    for j in range(i,n):
        U[i][j]=A[i][j] -sum(L[i][k]*U[k][j] for k in range(i))
        print(f"->Position {i}-{j}")
        dispmatrice(U)
    L[i][i]=1.0
    if i+1<n : print("Matrice L:") #If pour résoudre le problème de "Matrice L" dans le vide
    for j in range(i+1,n):
        print(f"->Position {i}-{j}")
        dispmatrice(L)
        L[j][i]=(A[j][i]-sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]

print("Matrices L et U finales:")
dispmatrice(L)
dispmatrice(U)

#Substitution avant, résolution de Ly=b
y= [0.0]*n
for i in range(n):
    somme = 0
    for j in range(i):
        somme+= L[i][j]*y[j]
    y[i]=(b[i]-somme)/L[i][i]
print("vecteur y: ")
dispvecteur(y)

#Substitution arrière, résolution de Ux=y
x = [0.0] * n
for i in range(n-1, -1, -1):
    somme = 0
    for j in range(i+1, n):
        somme += U[i][j] * x[j]
    x[i] = (y[i] - somme) / U[i][i]
print("vecteur x:")
dispvecteur(x)

#Vérification du résultat, consiste à multiplier A par x et à retrouver b si tout fonctionne
résultat = [] #vecteur résultat
for ligne in A:
    somme =0
    xcounter=0
    for colonne in ligne:
        somme+= colonne*x[xcounter]
        xcounter+=1
    résultat.append(somme)

print("vérification du résultat: ")
dispvecteur(résultat)
print("Le résultat est correct") if résultat == b else print("ATTENTION: le résultat n'est pas correct, il y a un bug")
