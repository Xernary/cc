#include <string.h>
#include <stdlib.h>
#include <stdio.h>
int main(int argn, char** args){

  if(argn != 2)
    exit(1);

  char flag[strlen(args[1])+1];

  int blocks = strlen(args[1]) / 4;

  for(int i = 0; i < blocks; i++){
    flag[i*4] = args[1][i*4 + 3];
    flag[i*4 + 1] = args[1][i*4 + 1];
    flag[i*4 + 2] = args[1][i*4 + 2];
    flag[i*4 + 3] = args[1][i*4];
  }

  flag[strlen(args[1])] = '\0'; 

  printf("%s\n", flag);

  return 0;
}
