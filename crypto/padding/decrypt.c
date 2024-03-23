#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argn, char** args){

  if(argn <= 1)
    exit(1);

  char* prompt = NULL;
  size_t buffer_size = 0;
  getline(&prompt, &buffer_size, stdin);
  printf("output: %s\n", prompt);

  return 0;
}
