#include <stdio.h>
#include <string.h>

#define N 3

double A[N][N] = {{2,3,1},{4,7,3},{6,18,5}}; // Matrice recherchée
double b[N] = {1,3,5};
double L[N][N];
double U[N][N];

void dispmatrice(double matrice[N][N]) {
    char chaine[256] = "";
    char buf[16];
    //Boucles pour parcourir la matrice
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            sprintf(buf, " %d ", (int)matrice[i][j]);
            strcat(chaine, buf); // Concatenne la chaine de caractères
        }
        strcat(chaine, "\n");
    }
    printf("%s", chaine);
}

void dispvecteur(double vecteur[N]) {
    for (int i = 0; i < N; i++)
        printf("%f\n", vecteur[i]);
}

int main() {

    // Initialisation de L et U à 0 (deux tableaux séparés pour éviter les problèmes d'adresse mémoire)
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            L[i][j] = 0;
            U[i][j] = 0;
        }

    //Décomposition LU, voir l'algorithme papier pour le détail des formules
    for (int i = 0; i < N; i++) {
        printf("Matrice U:\n");
        for (int j = i; j < N; j++) {
            double somme = 0.0;
            for (int k = 0; k < i; k++)
                somme += L[i][k] * U[k][j];
            U[i][j] = A[i][j] - somme;
            printf("->Position %d-%d\n", i, j);
            dispmatrice(U);
        }
        L[i][i] = 1.0;
        printf("Matrice L:\n");
        for (int j = i+1; j < N; j++) {
            printf("->Position %d-%d\n", i, j);
            dispmatrice(L);
            double somme = 0.0;
            for (int k = 0; k < i; k++)
                somme += L[j][k] * U[k][i];
            L[j][i] = (A[j][i] - somme) / U[i][i];
        }
    }
    printf("Matrices L et U finales:\n");
    dispmatrice(L);
    dispmatrice(U);

    //Substitution avant, résolution de Ly=b
    double y[N];
    for (int i = 0; i < N; i++) y[i] = 0.0;
    for (int i = 0; i < N; i++) {
        double somme = 0;
        for (int j = 0; j < i; j++)
            somme += L[i][j] * y[j];
        y[i] = (b[i] - somme) / L[i][i];
    }
    printf("vecteur y: \n");
    dispvecteur(y);

    //Substitution arrière, résolution de Ux=y
    double x[N];
    for (int i = 0; i < N; i++) x[i] = 0.0;
    for (int i = N-1; i >= 0; i--) {
        double somme = 0;
        for (int j = i+1; j < N; j++)
            somme += U[i][j] * x[j];
        x[i] = (y[i] - somme) / U[i][i];
    }
    printf("vecteur x:\n");
    dispvecteur(x);

    //Vérification du résultat, consiste à multiplier A par x et à retrouver b si tout fonctionne
    double resultat[N]; //vecteur résultat
    for (int i = 0; i < N; i++) {
        double somme = 0;
        int xcounter = 0;
        for (int j = 0; j < N; j++) {
            somme += A[i][j] * x[xcounter];
            xcounter++;
        }
        resultat[i] = somme;
    }
    printf("vérification du résultat: \n");
    dispvecteur(resultat);

    return 0;
}