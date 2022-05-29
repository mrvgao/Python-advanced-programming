#include<stdio.h>


int main(){
    int total=10;
    int acc = 0;
    for(int i = 0; i <= total; i++){
        acc += i;
    }
    printf("the result is %d\n", &acc);

    return 0;
}
