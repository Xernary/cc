#include <stdlib.h>
#include <stdio.h>

int main(){

  int result = -1;
  char* input = "helloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo";
  char* format = "%s";

  sscanf(input, format, &result);
  printf("%d\n", result);

  return 0;
}
