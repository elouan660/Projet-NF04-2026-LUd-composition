A = [[2,3,1],[4,7,3],[6,18,5]]
vecteur = [1,3,5]
L = [[1,0,0], [0,1,0],[0,0,1]]
U= [[0,0,0],[0,0,0],[0,0,0]]
def dispmatrice(matrice):
    chaine = ""
    for i in matrice:
        chaine+="\n"
        for j in i:
            chaine+= f" {int(j)} "
    print(chaine)
for i in range(3):
    print("Matrice U")
    for j in range(i,3):
        dispmatrice(U)
        U[i][j]=A[i][j] -sum(L[i][k]*U[k][j] for k in range(i))
    L[i][i]=1.0
    dispmatrice(U)
    print("Matrice L")
    for j in range(i+1,3):
        L[j][i]=(A[i][j]-sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]

print(f"{L} \n {U}")
dispmatrice(L)
