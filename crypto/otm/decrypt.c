#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void check_for_pattern(char* string){
    int size = strlen(string);
    for(int i = 0; i < size-3; i+=2){
      if(string[i] == string[i+2] && string[i+1] == string[i+3])
        printf("pattern found: %c%c at %d\n", string[i], string[i+1], i);
    }
}


int main(int argn, char** args){

  if(argn != 2)
    exit(1);

  char* path = args[1];
  FILE* fd;

  // Open a file in read mode
  fd = fopen(path, "r");

  // Store the content of the file
  char string[512];

  // Read the content and print it
  int size;
  while(fgets(string, 512, fd)) {
    // check for same pattern
    check_for_pattern(string);
    printf("%s", string);
  }

  // Close the file
  fclose(fd);
}
