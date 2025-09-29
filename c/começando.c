#include <stdio.h>

int main(){

    // IMPRIME O CABEÇALHO DO NOSSO JOGO
    printf("----------------------------------\n");
    printf("-Bem vindo ao jogo de adivinhação-\n");
    printf("----------------------------------\n");

    int numero_secreto = 42;

    int numero;

    printf("O numero secreto é: %d\n", numero_secreto);
    printf("Digite o numero secreto: ");
    scanf("%d", &numero);
    printf("O numero secreto que você digitou foi: %d", numero);

}
