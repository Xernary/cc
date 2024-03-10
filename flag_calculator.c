#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FLAG_SIZE 37
#define NUM_SIZE 8

int my_pow(int x, int y){
  int result = 1;
  for(int i = 0; i < y; i++){
    result = result * x;
  }
  return result;
}

int hex_to_dec(char* hex){

  int result = 0;
  int dec;
  for(int i = 0; i < strlen(hex)-1; i++){

    switch(hex[strlen(hex)-2-i]){

      case 'a':
      case 'A':
        dec = 10;
        break;
     
      case 'b':
      case 'B':
        dec = 11;
        break;

      case 'c':
      case 'C':
        dec = 12;
        break;

      case 'd':
      case 'D':
        dec = 13;
        break;

      case 'e':
      case 'E':
        dec = 14;
        break;

      case 'f':
      case 'F':
        dec = 15;
        break;

      default:
        dec =  hex[strlen(hex)-2-i] - '0';
        break;
    }
    result += (my_pow(16, i)) * dec;
  }
  return result;
}

int main(int argn, char** args){

  FILE *file;
  char num[8];
  int current = 0;
  char arr[FLAG_SIZE];

  // read from chars.txt file
  file = fopen("chars.txt", "r");
  int i = 0;
  while(fgets(num, NUM_SIZE, file)) {
    current = hex_to_dec(num) - current;
    arr[i] = current;
    current = hex_to_dec(num);
    printf("%c", arr[i]);
    i++;
  }
  printf("\n");
  fclose(file);


  return 0;
}
