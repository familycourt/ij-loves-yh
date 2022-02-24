//
// Created by 송인제 on 2022/02/24.
//

#include<stdio.h>

int main(){
    int N;


    scanf("%d",&N);

    for(int i=0; i<N; i++){
        for(int a=N-i-1; a>0; a--)
            printf(" ");
        for(int b=0; b<=i; b++)
            printf("*");
        for(int b=0; b<i; b++)
            printf("*");
        printf("\n");
    }

    return  0;
}
